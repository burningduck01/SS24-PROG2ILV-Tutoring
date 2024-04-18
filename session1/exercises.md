# Session 1

## exercise 1: OOP

### Part 1:

Create following Classes with specified attributes and implement `__init__` method for all specified attributes.

- **Zoo**
  - animals: list of Animal
  - employees: list of Employee

---

- **Employee**
  - name: String
- Zookeeper
  - is a Employee
- Vendor
  - is a Employee
  - sells: list of Strings

---

- **Animal**
  - name: String
  - food: String
  - favorite: Employee or None, if not defined None
- Monkey
  - is an Animal
- Alligator
  - is an Animal
  - hasEaten: list of Employee
- Horse
  - is an Animal
  - haircolor: String

---

### Part 2:

Add the following methods.

- get_employee search in the **Zoo** object, return the Employee object, if the name exists.
- add_employee should add an Employee object to the Zoo, each name should be unique (like an id, check if an emplyee with the given name already esists). Return an error if not posible.
- add_animal should add an Animal object to the Zoo. If favorite is defined, only add if an Employee with the given name exists. If it succeds return True, otherwise False.
- len() on the Zoo class should return the amount of animals in the zoo
- implement a representation, for printing the Zoo object, that returns `"{name} eats {food}"` for all animals in the Zoo object separated by a `,`.
- implement a methode for `==` to check of Employees or Animals have the same name.

---

### Part 3:

Create a class method for **Horse**, called `create()`, that uses an **Animal** object and an color as input and makes it to an Horse.

Create a class method for **Horse** that has **zoo** and **name** as an imput and returns the first Horse with said name.

## exercise 2: testing

Think about 5 different testcases for exercise 1:

- create a fixture that creates a zoo
- check the length of zoo
- check that you can't add an Employee twice
- check if add_employee raises an Error
- check if the printing/str return is correct
- usw.

## exercise 3: sockets

In the exercise 3 folder is already an exercise.py file defined, that if you want to use it, creates a **Server** object and executes the `run()` method in another thread. A **Client** object is also started by executing the `run()` method.

### Part 1:
Create a TCP Client Server connection, enabeling the Client sending a predifined message to the server and printing the recieved massage in the server console.

### Part 2:
Implement a multithreaded implimentation on the server side. Think of accepting in a loop and running the connection in another **Thread**.

### Part 3:
Create an message **Class**, that stores a **username** and **message**. Implement a method to enabling sending these attributes to the server in one message. On the Server use a **classmethode** to recreate the message object, then print only the sent message without the username.
