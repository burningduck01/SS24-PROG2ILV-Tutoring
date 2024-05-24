from random import randint
import time

def foo(n: int):
    r = randint(1, 100)
    time.sleep(n/r)


class MyTimer:
    shortest = None
    longest = None

    def __init__(self) -> None:
        self.rand = randint(0, 3)

    def __enter__(self) -> int:
        self.start = time.time()
        return self.rand

    def __exit__(self, exception, value, traceback):
        self.end = time.time()
        t = self.end - self.start
        t = round(t, 3)
        print(t)

        if self.__class__.shortest is None:
            self.__class__.shortest = t
            self.__class__.longest = t

        elif t < self.__class__.shortest:
            self.__class__.shortest = t
        elif t > self.__class__.longest:
            self.__class__.longest = t

    def __repr__(self) -> str:
        return f"shortest: {self.__class__.shortest}\nlongest: {self.__class__.longest}"
    

class MyOther(MyTimer):
    shortest = None
    longest = None


for _ in range(5):
    with MyTimer() as t:
        foo(t)

for _ in range(5):
    with MyOther() as t:
        foo(t)

print(MyTimer())
print(MyOther())