import socket
import pickle
from cryptography.fernet import Fernet, InvalidToken
import os

PyQt_import = True
try:
    from PyQt5.QtWidgets import QMessageBox
except (ImportError, QMessageBox):
    PyQt_import = False

IP = "127.0.0.1"  # The server's IP, blank to use the computers' public ip.
PORT = 6969  # General port is 6969, to upload files it's 6970 and to download files it's 6968
ADDR = (IP, PORT)


class DetailsNotCorrect(Exception):
    pass


class ServerNotRunning(Exception):
    pass


#  Make the output to the console be in colors.
class Color(object):
    def __init__(self):
        self.PURPLE = '\033[1;35;48m'
        self.CYAN = '\033[1;36;48m'
        self.BOLD = '\033[1;37;48m'
        self.BLUE = '\033[1;34;48m'
        self.GREEN = '\033[1;32;48m'
        self.YELLOW = '\033[1;33;48m'
        self.RED = '\033[1;31;48m'
        self.BLACK = '\033[1;30;48m'
        self.UNDERLINE = '\033[4;37;48m'
        self.END = '\033[1;37;0m'

    def red(self, string):
        return f"{self.RED}{string}{self.END}"

    def green(self, string):
        return f"{self.GREEN}{string}{self.END}"


color = Color()


class Client(object):
    # Client class, responsible for logging to account, signing up to a new account, list_files method,
    def __init__(self):
        self.__sock = socket.socket()
        try:
            self.__sock.connect(ADDR)
            self.__key = Fernet(self.__sock.recv(1024))
            self.__username = None
            self.__password = None
        except (WindowsError, InvalidToken):
            if PyQt_import:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("The Server is not running currently, please try again later!")
                msg.setWindowTitle("Error")
                msg.exec_()
                raise ServerNotRunning()
            else:
                raise ServerNotRunning(
                    "The Server is not running currently, btw you don't have PyQt5 installed, use \"pip install PYQt5\" to use the GUI version.")

    def login(self, username, password):
        self.__sock.send(self.__key.encrypt(b"login"))
        self.__sock.send(self.__key.encrypt(pickle.dumps({"username": username, "password": password})))
        response = pickle.loads(self.__key.decrypt(self.__sock.recv(1024)))
        if response:
            self.__username = username
            self.__password = password
            print(color.green(f"You have been successfully connected, {username}"))
        else:
            raise DetailsNotCorrect(color.red("The details you entered are incorrect unable to login"))
        return response

    def sign_up(self, username, password, email):
        self.__sock.send(self.__key.encrypt(b"sign_up"))
        self.__sock.send(self.__key.encrypt(pickle.dumps({"username": username, "password": password, "email": email})))
        response = pickle.loads(self.__key.decrypt(self.__sock.recv(1024)))
        return response

    def delete_user(self):
        self.__sock.send(self.__key.encrypt(b"delete_user"))
        self.__sock.send(self.__key.encrypt(pickle.dumps({"username": self.__username, "password": self.__password})))

    def upload(self, path):
        if isinstance(path, list):
            for p in path:
                UploadFiles(self.__username, self.__password, p)
        else:
            UploadFiles(self.__username, self.__password, path)

    def get_files(self):
        self.__sock.send(self.__key.encrypt(b"get_files"))
        files = pickle.loads(self.__key.decrypt(self.__sock.recv(4096)))
        print(files)
        return files


class UploadFiles(object):
    def __init__(self, username, password, path):
        self.IP = IP
        self.PORT = PORT + 1
        self.path = path
        self.__sock = socket.socket()
        self.__sock.connect((self.IP, self.PORT))
        self.__username = username
        self.__password = password
        self.__key: (Fernet, None) = None
        self.verify_details()

    def verify_details(self):
        self.__key = Fernet(self.__sock.recv(1024))
        self.__sock.send(self.__key.encrypt(pickle.dumps({"username": self.__username, "password": self.__password})))
        response: bool = pickle.loads(self.__key.decrypt(self.__sock.recv(1024)))
        if response:
            self.upload()
        else:
            raise DetailsNotCorrect()

    def upload(self):
        base_name = os.path.basename(self.path)  # e.g c:/user/Desktop/pic.png -> pic.png
        UploadFiles.copyfile(self.__key, self.path)
        self.__sock.send(self.__key.encrypt(base_name.encode()))
        with open(f"{self.path}.copy", "rb") as file:
            file_data = file.read(2048)
            while file_data:
                self.__sock.send(file_data)
                file_data = file.read(2048)
        print("Closing the connection, file uploaded")
        os.remove(f"{self.path}.copy")
        self.__sock.close()

    @staticmethod
    def copyfile(key, path):
        with open(path, "rb") as origin:
            with open(f"{path}.copy", "wb") as file:
                file.write(key.encrypt(origin.read()))


if __name__ == '__main__':
    pass
