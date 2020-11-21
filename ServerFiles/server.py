import json
import socket
from threading import Thread
import pickle
from cryptography.fernet import Fernet, InvalidToken
import re
import os

IP = "127.0.0.1"
PORT = 6969
ADDR = (IP, PORT)



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


def valid_email(email):
    return bool(re.search(r"[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email))


def add_user(user, email, password):
    with open("users.json") as fr:
        data = json.load(fr)
        data[user] = {"email": email, "password": password}
        with open("users.json", "w") as fw:
            json.dump(data, fw, indent=4)
    os.mkdir(user)


def user_exists(user):
    with open("users.json") as f:
        data = json.load(f)
        try:
            _ = data[user]
            return True
        except KeyError:
            return False


def email_exists(email):
    with open("users.json") as f:
        data = json.load(f)
    for i in data.values():
        if i["email"] == email:
            return True
    return False


def new_client(client, key):
    Client(client, key)


def end_thread(thread):
    thread.join()


class Server(object):
    def __init__(self):
        self.server = socket.socket()
        self.server.bind(ADDR)
        self.server.listen()
        print("[+] Server Listening")

    def accept_conns(self):
        while True:
            client, _ = self.server.accept()
            key = Fernet.generate_key()
            client.send(key)
            key = Fernet(key)
            print("client connected")
            client_thread = Thread(target=new_client, args=(client, key))
            client_thread.start()


class Client(object):
    def __init__(self, client: socket.socket, key: Fernet):
        self.__client = client
        self.__key = key
        self.__username: (str, None) = None
        self.__password: (str, None) = None
        self.__HEADERS: dict = {
            b"login": self.login,
            b"sign_up": self.sign_up,
            b"delete_user": self.delete_user,
            b"get_files": self.get_files
        }
        self.recieve_header()

    def recieve_header(self):
        while True:
            try:
                header = self.__client.recv(4096)
                try:
                    self.__HEADERS[self.__key.decrypt(header)]()
                except (InvalidToken, KeyError):
                    # when a client disconnects, empty bytes are being sent. This checks if the header is not of length zero.
                    if not header:
                        self.__client.close()
                        print(f"client \"{self.__username}\" was closed")
                        break
                    continue
            except ConnectionResetError:
                break

    def login(self):
        try:
            user_data: dict = pickle.loads(self.__key.decrypt(self.__client.recv(2048)))
            with open("users.json") as f:
                users = json.load(f)
            if user_exists(user_data['username']):
                if users[user_data["username"]]["password"] == user_data["password"]:
                    self.__client.send(self.__key.encrypt(pickle.dumps(True)))
                    self.__username = user_data['username']
                    self.__password = user_data['password']
                    print(color.green(f"Client: {user_data['username']} connected!"))
                else:
                    self.__client.send(self.__key.encrypt(pickle.dumps(False)))
            else:
                self.__client.send(self.__key.encrypt(pickle.dumps(False)))
        except ConnectionResetError:
            print("Someone Left...")

    def sign_up(self):
        client = self.__client
        key = self.__key
        try:
            user_data = pickle.loads(key.decrypt(client.recv(2048)))
            if not user_exists(user_data["username"]):
                if len(user_data["username"]) > 4 and valid_email(user_data["email"]) and not email_exists(
                        user_data["email"]):
                    add_user(user_data["username"], user_data["email"], user_data["password"])
                    client.send(key.encrypt(pickle.dumps(True)))
                else:
                    raise IndexError
            else:
                raise IndexError
        except Exception or IndexError:
            client.send(key.encrypt(pickle.dumps(False)))

    def delete_user(self):
        with open("users.json") as f:
            users = json.load(f)
        user_data = pickle.loads(self.__key.decrypt(self.__client.recv(2048)))
        if users[user_data["username"]]["password"] == user_data["password"]:
            users.pop(user_data["username"].encode().decode())
            with open("users.json", "w") as fw:
                json.dump(users, fw, indent=4)

    def get_files(self):
        files = [f for f in os.listdir(f"{self.__username}\\") if os.path.isfile(os.path.join(f"{self.__username}\\", f)) and not f.endswith(".n")]
        self.__client.send(self.__key.encrypt(pickle.dumps(files)))



class UploadFilesServer(object):
    def __init__(self):
        self.PORT = PORT + 1
        self.IP = IP
        self.upload_server = socket.socket()
        self.upload_server.bind((self.IP, self.PORT))
        self.upload_server.listen()

    def accept_conns(self):
        while True:
            client, _ = self.upload_server.accept()
            key = Fernet.generate_key()
            client.send(key)
            key = Fernet(key)
            Thread(target=lambda: ClientUpload(client, key)).start()


class ClientUpload(object):
    def __init__(self, client, key):
        self.__client = client
        self.__key = key
        self.__username = None
        self.__password = None
        self.file_name = None
        self.verify_details()

    def verify_details(self):
        user_data: dict = pickle.loads(self.__key.decrypt(self.__client.recv(2048)))
        with open("users.json") as f:
            users = json.load(f)
        if user_exists(user_data['username']):
            if users[user_data["username"]]["password"] == user_data["password"]:
                self.__client.send(self.__key.encrypt(pickle.dumps(True)))
                self.__username = user_data['username']
                self.__password = user_data['password']
                self.recieve_file_data()
            else:
                self.__client.send(self.__key.encrypt(pickle.dumps(False)))
        else:
            self.__client.send(self.__key.encrypt(pickle.dumps(False)))


    def recieve_file_data(self):
        self.file_name = self.__key.decrypt(self.__client.recv(1024)).decode()
        with open(f"{self.__username}\\{self.file_name}.n", "wb") as file:
            while True:
                file_data = self.__client.recv(4096)
                if not file_data:
                    break
                file.write(file_data)
        with open(f"{self.__username}\\{self.file_name}.n", "rb") as encrypted_file:
            with open(f"{self.__username}\\{self.file_name}", "wb") as file_to_write:
                file_to_write.write(self.__key.decrypt(encrypted_file.read()))
        os.remove(f"{self.__username}\\{self.file_name}.n")




if __name__ == '__main__':
    server = Server()
    Thread(target=server.accept_conns).start()
    server2 = UploadFilesServer()
    Thread(target=server2.accept_conns).start()

