import json
import socket
from threading import Thread
import pickle
from cryptography.fernet import Fernet, InvalidToken
import re
import os
from color import Color
from yapf.yapflib.yapf_api import FormatFile

IP = "127.0.0.1"
PORT = 6969
ADDR = (IP, PORT)

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


def create_client_obj(client, key):
    client_obj = ClientProtocols()
    client_obj.init_client(client, key)


class Server(object):
    def __init__(self):
        self.server = socket.socket()
        self.server.bind(ADDR)
        self.server.listen(5)
        print("[+] Server Listening")

    def accept_conns(self):
        while True:
            client, _ = self.server.accept()
            key = Fernet.generate_key()
            client.send(key)
            key = Fernet(key)
            print("client connected")
            Thread(target=create_client_obj, args=(client, key)).start()



class ClientProtocols(object):
    def __init__(self):
        self.key, self.client, self.HEADERS = None, None, None
        self.username: str = ''
        self.opened_file: str = ''

    def init_client(self, client: socket.socket, key: Fernet):
        self.key: Fernet = key
        self.client: socket.socket = client
        self.HEADERS: dict = {
            b"login": self.login,
            b"sign_up": self.sign_up,
            b"file": self.upload_file,
            b"delete_user": self.delete_user
        }
        self.await_client_cmd()

    def await_client_cmd(self):
        while True:
            try:
                header: bytes = self.client.recv(2048)
                if header:
                    header = self.key.decrypt(header)
                    print(header)
                else:
                    continue
                if header.startswith(b"endfile"):



                self.HEADERS[header]() if header.split()[0] != b"file" else self.upload_file(header)
                print(f"HEADER IS {header}")
            except (InvalidToken, KeyError, ConnectionResetError, TypeError):
                continue


    def login(self):
        try:
            user_data: dict = pickle.loads(self.key.decrypt(self.client.recv(2048)))
            with open("users.json") as f:
                users = json.load(f)
            if user_exists(user_data['username']):
                if users[user_data["username"]]["password"] == user_data["password"]:
                    self.client.send(self.key.encrypt(pickle.dumps(True)))
                    self.username = user_data['username']
                    print(color.green(f"Client: {user_data['username']} connected!"))
                else:
                    self.client.send(self.key.encrypt(pickle.dumps(False)))
            else:
                self.client.send(self.key.encrypt(pickle.dumps(False)))
        except ConnectionResetError:
            print("Someone Left...")


    def sign_up(self):
        client = self.client
        key = self.key
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

    def upload_file1(self):
        """"{username: null, file_name: null}"""
        try:
            user_data = pickle.loads(self.key.decrypt(self.client.recv(2048)))
            print(color.green(f"client {user_data['username']} is trying to send {user_data['file_name']}"))
            with open(f"{user_data['username']}\\{user_data['file_name']}", "wb") as f:
                while True:
                    file_data = self.client.recv(4096).decode().encode()
                    if file_data:
                        file_data = self.key.decrypt(file_data)
                    else:
                        print(color.red(f"continuing with: {file_data}"))
                        continue
                    if file_data != b"endfile":
                        print(f'receiving data from {user_data["username"]}')
                        f.write(file_data)
                    else:
                        print("break")
                        break

        except Exception as e:
            print(e)


    def upload_file(self, header: bytes):
        print("here")
        header = header.decode().split()
        with open(f"{self.username}\\{header[1]}", mode="a+", newline="\r\n") as file:
            print("Recieved a file")
            self.opened_file = header[1]
            file.write(" ".join(header[2:]))


    def end_file(self):
        if self.opened_file:




    def delete_user(self):
        with open("users.json") as f:
            users = json.load(f)
        user_data = pickle.loads(self.key.decrypt(self.client.recv(2048)))
        if users[user_data["username"]]["password"] == user_data["password"]:
            users.pop(user_data["username"].encode().decode())
            with open("users.json", "w") as fw:
                json.dump(users, fw, indent=4)


#
#
# def sign_up(self, client, key):
#     self.null = 5
#     try:
#         user_data = pickle.loads(key.decrypt(client.recv(2048)))
#         if not check_exists(user_data["username"]):
#             if len(user_data["username"]) > 4 and valid_email(user_data["email"]) and not email_exists(
#                     user_data["email"]):
#                 add_user(user_data["username"], user_data["email"], user_data["password"])
#                 client.send(key.encrypt(pickle.dumps(True)))
#             else:
#                 raise IndexError
#         else:
#             raise IndexError
#     except Exception or IndexError:
#         client.send(key.encrypt(pickle.dumps(False)))
#
#
# def delete_user(self, client, key):
#     self.null = 5
#     with open("users.json") as f:
#         users = json.load(f)
#     user_data = pickle.loads(key.decrypt(client.recv(2048)))
#     if users[user_data["username"]]["password"] == user_data["password"]:
#         users.pop(user_data["username"].decode())
#         with open("users.json", "w") as fw:
#             json.dump(users, fw, indent=4)


def upload_file1(self, client, key):
    """"{username: null, file_name: null}"""
    self.null = 5
    try:
        user_data = pickle.loads(key.decrypt(client.recv(2048)))
        print(f"client {user_data['username']} is trying to send {user_data['file_name']}")
        with open(f"{user_data['username']}\\{user_data['file_name']}", "wb") as f:
            while True:
                file_data = key.decrypt(client.recv(4096))
                print(file_data)
                if file_data != b"end":
                    print(f'receiving data from {user_data["username"]}')
                    f.write(file_data)
                else:
                    break
    except Exception as e:
        print(e)
#
#
# def upload_file(self, client, key):
#     user_data = pickle.loads(key.decrypt(client.recv(2048)))
#     with open(f"{user_data['username']}\\{user_data['file_name']}", "wb") as f:
#         f.write(key.decrypt(p(client.recv(2048))))
#         f.write(key.decrypt(p(client.recv(2048))))
#
#
# def p(j):
#     print(j)
#     return j


def main():
    server = Server()
    Thread(target=server.accept_conns).start()


if __name__ == "__main__":
    main()
