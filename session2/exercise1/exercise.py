from threading import Thread
import socket

class Server:
    def __init__(self) -> None:
        pass

class Client:
    def __init__(self) -> None:
        pass

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
    