from random import randint
import time

def foo(n: int):
    r = randint(1, 100)
    time.sleep(n/r)


for _ in range(5):
    with MyTimer() as t:
        foo(t)
print(MyTimer())