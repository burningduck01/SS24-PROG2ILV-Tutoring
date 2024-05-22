@decorator_function("begin", "end")
def foo() -> None:
    print("- foo -")

@decorator_class("begin", "end")
def bar() -> None:
    print("- bar -")

foo()
bar()