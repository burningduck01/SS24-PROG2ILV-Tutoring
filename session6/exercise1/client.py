import socket
import pickle
from time import sleep

from task import Task

tasks = [Task("Test", "Dwight"),
         Task("Finance", "Michael", {"cashflow": 302.43}),
         Task("Absend", "Jim", {"for (in days)": 5})]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 5050))

for t in tasks:
    p = pickle.dumps(t)
    sock.send(b"PUT" + p)
    sleep(0.5)


sock.send(b"GET")
msg = sock.recv(1024)
task = pickle.loads(msg)
print(task)