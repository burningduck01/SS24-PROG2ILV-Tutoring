import socket
import threading

from message import Message

# connection handler: function to be called in new thread
def connection_handler(con: socket.socket, addr: socket.AddressInfo):
    print("connection to:", addr)

    running = True
    while running:
        # waiting to recieve message from client
        msg = con.recv(1024) 

        # cliend sends an empty msg, when closing connection -> stop loop
        if msg == bytes(b""):
            running = False
            print("closing connection to:", addr)
        else:
            # parse msg into an Message object, print it
            print(Message.parse(msg))

# create socket and listen to connections
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 5051))
sock.listen()

# loop to always accept new connection in a new thread
while True:
    con, addr = sock.accept()
    threading.Thread(target=connection_handler, args = (con, addr)).start() 

