from typing import List, Tuple
from random import shuffle

class MatchIterator:
    pass
    
def MatchGenerator():
    pass

if __name__ == "__main__":
    for name in MatchIterator(["John", "Max", "Kate", "Anna"], ["Doe", "Mustermann"], 9):
        print(name)

    print("-"*5)

    for name in MatchGenerator(["John", "Max", "Kate", "Anna"], ["Doe", "Mustermann"], 9):
        print(name)