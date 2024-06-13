from typing import List
from datetime import datetime
import pickle

class Task:
    def __init__(self, name: str, creator: str, data: dict = {}) -> None:
        self.name: str = name
        self.creator: str = creator
        self.times: List[datetime] = [datetime.now()]
        self.data: dict = data

    def __repr__(self) -> str:
        return self.name + f" is waiting for: {len(self)}"
    
    def __len__(self) -> int:
        delta = datetime.now() - self.times[0]
        return int(delta.microseconds)

if __name__ == "__main__":
    t1 = Task("Test", "admin")
    print(t1)

    p = pickle.dumps(t1)
    print(p)

    t2 = pickle.loads(p)
    print(t2)