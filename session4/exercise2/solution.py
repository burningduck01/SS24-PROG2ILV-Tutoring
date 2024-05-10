def myGenerator(ls: list):
    for i in range(0, len(ls), 2):
        yield ls[i]

my = myGenerator(["A", "B", "C", "D", "E", "F"])
for i in my:
    print(i)