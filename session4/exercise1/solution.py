from __future__ import annotations
from typing import List
from uuid import uuid1

class Customer:
    def __init__(self, name: str, contact: str) -> None:
        self.id = uuid1()
        self.name: str = name
        self.contact: str = contact
        self.items: List[Item] = []

    def add(self, item: Item | List[Item]) -> None:
        if isinstance(item, Item):
            self.items.append(item)
        elif isinstance(item, list):
            self.items = self.items + item
        else:
            raise ValueError
        
    def __repr__(self) -> str:
        items = [str(i) for i in self.items]
        items = "\n".join(items)
        return self.name + ":\n" + items

class Item:
    def __init__(self, description: str, value: float) -> None:
        self.id = uuid1()
        self.description: str = description
        self.value: float = value

    def __repr__(self) -> str:
        return f"{self.value}: {self.description}"


c = Customer("Max", "max@mustermann.at")
i1 = Item("Anciant Vase", 37.5)
i2 = Item("Magic Table", 293480)
i3 = Item("Special Coin", 1.3)
c.add([i1, i2, i3])

print(c)