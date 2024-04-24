from threading import Thread
import socket

class Server:
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        pass

class Client:
    def __init__(self) -> None:
        pass
        
    def run(self) -> None:
        pass

#####
import sys
# from threading import Thread
if __name__ == "__main__":
    if len(sys.argv) == 1:
    # if no commandline argument run server in other thread and run client
        Thread(target=Server().run).start()
        Client().run()
    elif len(sys.argv) == 2 and sys.argv[1] in ["server", "s"]:
    # run server if argument server or s
        Server().run()
    elif len(sys.argv) == 2 and sys.argv[1] in ["client", "c"]:
    # run client if argument client or c
        Client().run()
    