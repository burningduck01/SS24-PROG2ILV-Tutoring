from __future__ import annotations
from typing import List
from uuid import uuid1

from sqlalchemy import create_engine, Column, UUID, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(UUID, primary_key = True)
    name = Column(String)
    contact = Column(String)
    items = relationship("Item", backref = "customer")

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

class Item(Base):
    __tablename__ = "items"
    id = Column(UUID, primary_key = True)
    description = Column(String)
    value = Column(Float)
    customer_id = Column(UUID, ForeignKey("customers.id"))

    def __init__(self, description: str, value: float) -> None:
        self.id = uuid1()
        self.description: str = description
        self.value: float = value

    def __repr__(self) -> str:
        return f"{self.value}: {self.description}"


if __name__ == "__main__":
    c = Customer("Max", "max@mustermann.at")
    i1 = Item("Anciant Vase", 37.5)
    i2 = Item("Magic Table", 293480)
    i3 = Item("Special Coin", 1.3)
    c.add([i1, i2, i3])

    ##

    engine = create_engine("sqlite:///database.db", echo = True)
    Base.metadata.create_all(engine)
    SessionClass = sessionmaker(bind = engine)
    session = SessionClass()

    session.add(c)
    session.commit()