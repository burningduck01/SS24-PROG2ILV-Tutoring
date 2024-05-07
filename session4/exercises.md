# Session 4

## exercise 1: OOP

You are owner of an antique store:
Create an customer class, that stores following information about customers:

- id (UUID, primary identifier)
- name (string)
- contact (string, could be either email or telefonnumber)
- items (list of item class)
  - id (UUID, primary identifier)
  - description (string)
  - value (number)

Implement a representation function, that enables fancy printing of the class (name + items).

## exercise 1.1: json serialization

Copy the file from exercise 1 and modify it:
For exporting this object from your system, create json serilization and dump an object from this class into an file.

## exercise 1.2: SQL Alchemy

Copy the file from exercise 1 and modify it:
Integrate SQLAlchemy, so you can store this class into the database and retrieve it again.

## exercise 2: Generators

What's the difference between iterators and generators? Parallel to last session: Implement an generator function, using list as a function parameter, yield each element of the list.