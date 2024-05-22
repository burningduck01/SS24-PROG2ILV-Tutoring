# Session 5

## exercise 1: Exceptions

Given is a function called `foo` that, when called, randomly either prints `True`, `False` or trys to raise an exception called `MyException` with the parameter `r`.

- Implement `MyException`
- Write code that:
  - Always calles the `foo` function
  - If it doesn't fail print **"It works!"**
  - If it fails prints the **exception** with the parameter `r` (you maybe wannt to implement a fitting representation function)
  - No matter if it fails or not, print **"Always print this"**

## exercise 2: Context Managers

Given is the function `foo` that sleeps a random amount of time between `0` and the parameter `n`. Likewise a loop, that runs `foo` **5** times inside the context manager using `MyTimer`.

- Create the `MyTimer` class
- When run inside a context, return a `randint(0, 3)` (the variable `t` needed for calling the `foo` function)
- Store in a class variable the longest and the shortest loop time
- In the context calculate the time needed using `time.time()`
- Check that printing an instance of the class prints the shortest and the longest (stored in the class variable)

## exercise 3: Decorator

Given are a decorated `foo` and `bar` function.

- Implement a decorator **function** for the `foo` function to print the argument **"begin"** before and **"end"** after the `foo` function call.
- Implement a decorator **class** for the `bar` function similar to the decorator function for the `foo` function.

Secondly:

- Modify both decorators to implement the functools wraps decorator