import socket

# import message class
from message import Message

# create object and establish connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 5051))

# create Massage and send object encoded (as defined in the Message class)
msg = Message("Chewbacca", "Hello World!")
sock.sendall(msg.encode())