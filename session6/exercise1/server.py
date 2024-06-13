import socket
import pickle
from datetime import datetime
from typing import List
from threading import Thread

from task import Task
tasks: List[Task] = []

def handler(conn: socket.socket, addr: socket.AddressInfo):
    print("cnnected to: ", addr)

    while True:
        msg = conn.recv(1024)

        if msg == b"GET":
            t = tasks.pop(0)
            t.times.append(datetime.now())
            p = pickle.dumps(t)
            print("sent: ", t)
            conn.send(p)

        elif msg[:3] == b"PUT":
            t: Task = pickle.loads(msg[3:])
            print("got: ", t)
            t.times.append(datetime.now())
            tasks.append(t)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 5050))

sock.listen()
while True:
    conn, addr = sock.accept()
    Thread(target = handler, args = (conn, addr), daemon = True).start()