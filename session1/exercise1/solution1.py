from typing import List

class Zoo:
    def __init__(self) -> None:
        self.animals: List[Animal] = []
        self.employees: List[Employee] = []

### Employees
class Employee:
    def __init__(self, name: str) -> None:
        self.name = name

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