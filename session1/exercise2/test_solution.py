import pytest

from session1.exercise1.solution3 import *


@pytest.fixture
def zoo():
    z = Zoo()
    z.add_animal(Monkey("Yoda", "Banana"))
    z.add_animal(Monkey("Mace", "Banana"))

    # not able to add Anakin, because no Employee Obi-Wan exists.
    z.add_animal(Monkey("Anakin", "Banana", Zookeeper("Obi-Wan")))
    return z


def test_add(zoo: Zoo):
    assert len(zoo) == 2

    zoo.add_employee(Zookeeper("Obi-Wan"))
    zoo.add_animal(Monkey("Anakin", "Banana", Zookeeper("Obi-Wan")))
    assert len(zoo) == 3
    

def test_error(zoo: Zoo):
    zoo.add_employee(Zookeeper("Obi-Wan"))

    with pytest.raises(LookupError):
        zoo.add_employee(Zookeeper("Obi-Wan"))


def test_print(capfd, zoo: Zoo):
    assert str(zoo) == "Yoda eats Banana, Mace eats Banana"

    # gets the console output for assertion
    print(zoo)
    out, _ = capfd.readouterr()
    assert out == "Yoda eats Banana, Mace eats Banana\n"


def test_eq():
    assert Zookeeper("Obi-Wan") == Zookeeper("Obi-Wan")
    assert Zookeeper("Obi-Wan") != Zookeeper("Wan-Obi")