from __future__ import annotations
from typing import List

class Zoo:
    def __init__(self) -> None:
        self.animals: List[Animal] = []
        self.employees: List[Employee] = []

    def get_employee(self, name: str) -> Employee | None:
        for e in self.employees:
            if e.name == name:
                return e

    def add_employee(self, employee: Employee) -> None:
        if self.get_employee(employee.name) is None:
            self.employees.append(employee)
        
        else:
            raise LookupError
        
    def add_animal(self, animal: Animal) -> bool:
        if animal.favorite is None or self.get_employee(animal.favorite.name) is not None:
            self.animals.append(animal)
            return True
        
        else:
            return False
        
    def __len__(self) -> int:
        return len(self.animals)
    
    def __repr__(self) -> str:
        return ", ".join([a.name + " eats " + a.food for a in self.animals])
    

### Employees
class Employee:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def __eq__(self, value: object) -> bool:
        return self.name == value.name

class Zookeeper(Employee):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class Vendor(Employee):
    def __init__(self, name: str, sells: List[str]) -> None:
        super().__init__(name)

        self.sells: List[str] = sells

### Animals
class Animal:
    def __init__(self, name: str, food: str, employee: Employee | None = None) -> None:
        self.name: str = name
        self.food: str = food
        self.favorite: Employee | None = employee

    def __eq__(self, value: object) -> bool:
        return self.name == value.name

class Monkey(Animal):
    def __init__(self, name: str, food: str, employee: Employee | None = None) -> None:
        super().__init__(name, food, employee)

class Alligator(Animal):
    def __init__(self, hasEaten: Employee | List[Employee], name: str, food: str, employee: Employee | None = None) -> None:
        super().__init__(name, food, employee)

        if not isinstance(hasEaten, list):
            hasEaten = [hasEaten]
        self.hasEaten: List[Employee] = hasEaten

class Horse(Animal):
    def __init__(self, color: str, name: str, food: str, employee: Employee | None = None) -> None:
        super().__init__(name, food, employee)

        self.haircolor: str = color