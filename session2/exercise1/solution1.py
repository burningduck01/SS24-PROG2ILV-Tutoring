from threading import Thread
import socket

class Server:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("localhost",5050))
        self.sock.listen()

        conn, _ = self.sock.accept()
        msg = conn.recv(1024)
        print(msg.decode())


class Client:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("localhost", 5050))

        self.sock.send(b"Hello World!")


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
    