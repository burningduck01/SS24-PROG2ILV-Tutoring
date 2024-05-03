import socket

server_addr = ("localhost", 5051)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_addr)

while True:
    msg, client_addr = sock.recvfrom(1024)
    msg = msg.decode()
    print("Request:", msg)

    msg = "\"" + msg + "\" acknowledged"
    msg = msg.encode()
    sock.sendto(msg, client_addr)

