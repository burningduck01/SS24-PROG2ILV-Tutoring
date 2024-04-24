from __future__ import annotations
from threading import Thread
from time import sleep
import socket

class Server:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("localhost",5050))
        self.sock.listen()

        while True:
            conn, addr = self.sock.accept()
            Thread(target=self.connection_handler, args = (conn, addr)).start()

    def connection_handler(self, con: socket.socket, addr: socket.AddressInfo) -> None:
        print("connection to:", addr)

        running = True
        while running:
            msg = con.recv(1024) 

            if msg == bytes(b""):
                running = False
                print("closing connection to:", addr)
            else:
                print(Message.parse(msg))

class Client:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("localhost", 5050))

        sleep(1)
        msg = Message("admin", "Hello World!")
        self.sock.send(msg.encode())
        sleep(1)
        

class Message:
    def __init__(self, user: str, msg: str) -> None:
        self.message = msg
        self.user = user

    def encode(self) -> bytes:
        msg =  "|".join([self.user, self.message])
        msg = msg.encode()
        return msg
    
    @classmethod
    def parse(cls, msg:bytes) -> Message:
        msg = msg.decode()
        msg = msg.split("|")

        msg = Message(*msg)
        return msg
    
    def __repr__(self) -> str:
        return f"[{self.user}]: {self.message}"


#####
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
    # if no commandline argument run server in other thread and run client
        Thread(target=Server, daemon = True).start()
        Client()
    elif len(sys.argv) == 2 and sys.argv[1] in ["server", "s"]:
    # run server if argument server or s
        Server()
    elif len(sys.argv) == 2 and sys.argv[1] in ["client", "c"]:
    # run client if argument client or c
        Client()
    