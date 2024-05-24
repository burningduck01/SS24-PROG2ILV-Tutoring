class MyException(Exception):
    def __init__(self, n: int, *args: object) -> None:
        super().__init__(*args)
        self.n: int = n

    def __str__(self) -> str:
        return self.__class__.__name__ + f": Failed because of {self.n}"


def foo():
    from random import randint
    r = randint(0, 5)
    if r > 1:
        raise MyException(r)
    else:
        print(bool(r))


try:
    foo()
except MyException as e:
    print(e)
else:
    print("It works!")
finally:
    print("Always print this")