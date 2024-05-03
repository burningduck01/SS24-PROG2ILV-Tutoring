import socket

addr_client = ("localhost", 5050)
addr_server = ("localhost", 5051)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr_client)

while True:
    msg = input("Request: ")
    msg = msg.encode()
    sock.sendto(msg, addr_server)

    msg, _ = sock.recvfrom(1024)
    msg = msg.decode()
    print("Response:", msg)