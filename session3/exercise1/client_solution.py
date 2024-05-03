import socket

client_addr = ("localhost", 5050)
server_addr = ("localhost", 5051)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(client_addr)

while True:
    msg = input("Request: ")
    msg = msg.encode()
    sock.sendto(msg, server_addr)

    msg, _ = sock.recvfrom(1024)
    msg = msg.decode()
    print("Response:", msg)