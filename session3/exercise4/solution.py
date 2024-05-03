class MyList:
    def __init__(self, ls: list) -> None:
        self.list = ls

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1

        if self.n >= len(self.list)+1:
            raise StopIteration
        else:
            return self.list[self.n-1]

my = MyList(["a", "b", "c", "d", "e", "f"])
for a in my:
    print(a)