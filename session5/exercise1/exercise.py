def foo():
    from random import randint
    r = randint(0, 5)
    if r > 1:
        raise MyException(r)
    else:
        print(bool(r))