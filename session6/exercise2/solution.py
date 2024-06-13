from typing import List, Tuple
from random import shuffle

class MatchIterator:
    def __init__(self, firstnames: List[str], lastnames: List[str], stop: int) -> None:
        self.firstnames: List[str] = firstnames
        self.lastnames: List[str] = lastnames
        self.stop: int = stop

        self.matches: List[Tuple[str, str]] = [(first, last) for last in self.lastnames for first in self.firstnames]
        shuffle(self.matches)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n >= self.stop or self.n >= len(self.matches):
            raise StopIteration
        else:
            try:
                return self.matches[self.n]
            finally:
                self.n += 1
    
def MatchGenerator(firstnames: List[str], lastnames: List[str], stop: int):
        matches: List[Tuple[str, str]] = [(first, last) for last in lastnames for first in firstnames]
        shuffle(matches)

        n = 0
        while n < stop and n < len(matches):
            try:
                yield matches[n]
            finally:
                n += 1

if __name__ == "__main__":
    for name in MatchIterator(["John", "Max", "Kate", "Anna"], ["Doe", "Mustermann"], 9):
        print(name)

    print("-"*5)

    for name in MatchGenerator(["John", "Max", "Kate", "Anna"], ["Doe", "Mustermann"], 9):
        print(name)