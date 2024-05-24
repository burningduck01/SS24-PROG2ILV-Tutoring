from functools import wraps

def decorator_function(begin: str, end: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(begin)
            result = func(*args, **kwargs)
            print(end)
            return result
        return wrapper
    return decorator


class decorator_class:
    def __init__(self, begin: str, end: str) -> None:
        self.begin = begin
        self.end = end

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(self.begin)
            result = func(*args, **kwargs)
            print(self.end)
            return result
        return wrapper


@decorator_function("hello", "bye")
def foo() -> None:
    print("- foo -")

@decorator_class("begin", "end")
def bar() -> None:
    print("- bar -")

foo()
bar()