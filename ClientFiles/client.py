import socket
import pickle
from cryptography.fernet import Fernet
from PyQt5.QtWidgets import QMessageBox
import os
from color import Color

IP = "127.0.0.1"
PORT = 6969
ADDR = (IP, PORT)

color = Color()


class ServerNotRunning(Exception):
    pass




class Client(object):
    def __init__(self):
        self.__sock = socket.socket()
        try:
            self.__sock.connect(ADDR)
            self.__key = Fernet(self.__sock.recv(1024))
        except WindowsError or Exception:
            if __name__ == "__main__":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("The Server is not running currently, please try again later!")
                msg.setWindowTitle("Error")
                msg.exec_()
                raise ServerNotRunning()
            else:
                print(color.red(f"The Server is not running currently, please try again later!"))
                exit(1)

    def login(self, username, password):
        self.__sock.send(self.__key.encrypt(b"login"))
        self.__sock.send(self.__key.encrypt(pickle.dumps({"username": username, "password": password})))
        response = pickle.loads(self.__key.decrypt(self.__sock.recv(1024)))
        if response:
            print(color.green(f"You have been successfully connected, {username}"))
        else:
            print(color.red("The details you entered are incorrect unable to login"))
        return response

    def sign_up(self, username, password, email):
        self.__sock.send(self.__key.encrypt(b"sign_up"))
        self.__sock.send(self.__key.encrypt(pickle.dumps({"username": username, "password": password, "email": email})))
        response = pickle.loads(self.__key.decrypt(self.__sock.recv(1024)))
        return response

    def delete_user(self, username, password):
        self.__sock.send(self.__key.encrypt(b"delete_user"))
        self.__sock.send(self.__key.encrypt(pickle.dumps({"username": username, "password": password})))

    def upload(self, path, username):
        try:
            file_name = os.path.basename(path)
            file_size = os.path.getsize(path)
            self.__sock.send(self.__key.encrypt(b"upload_file"))
            self.__sock.send(self.__key.encrypt(pickle.dumps({"username": username, "file_name": file_name, "file_size": file_size})))
            with open(path, "rb") as file:
                temp = file.read(2048)
                while temp:
                    self.__sock.send(self.__key.encrypt(temp))
                    temp = file.read(2048)
            return True
        except Exception or FileNotFoundError:
            return False

    def upload_file1(self, path, username):
        file_name = os.path.basename(path)
        self.__sock.send(self.__key.encrypt(b"upload_file"))
        self.__sock.send(self.__key.encrypt(pickle.dumps({"username": username, "file_name": file_name})))
        with open(path, "rb") as file:
            temp = file.read(2048)
            while temp:
                self.__sock.send(self.__key.encrypt(temp))
                temp = file.read(2048)
            self.__sock.send(self.__key.encrypt(b"endfile"))

    def upload_file(self, path, username):
        file_name = os.path.basename(path)

        with open(path, "rb") as file:
            file_data = file.read(2048)
            while file_data:
                self.__sock.send(self.__key.encrypt(f"file {file_name} ".encode() + file_data))
                file_data = file.read(2048)
        self.__sock.send(self.__key.encrypt(f"endfile {file_name}".encode()))


if __name__ == '__main__':
    client = Client()
    client.login("itayd", "i")
    client.upload_file("test.py", "itay")





