import socket

addr_server = ("localhost", 5051)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(addr_server)

while True:
    msg, addr_client = sock.recvfrom(1024)
    msg = msg.decode()
    print("Request:", msg)

    msg = "\"" + msg + "\" acknowledged"
    msg = msg.encode()
    sock.sendto(msg, addr_client)

