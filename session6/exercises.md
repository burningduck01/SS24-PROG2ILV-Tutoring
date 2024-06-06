# Session 6

## exercise 1: OOP + Network + Persistency

You are working in a company and get instructed to develop a python based system for task queueing:

- Generate a **Task** object that stores:
  - Name of task
  - Names of creator
  - Timestamps for creation, received at server, distribution to user
  - Data as a dictionary
- Create a **TCP Client/Server** network that allows multiple connections at the same time using **sockets** and implment following actions (add to the beginning of the sent message):
  - PUT Add one task to the server
  - GET Get the oldest task from the server
- Use **Pickle** for converting the Task object.

## exercise 2: Iterators / Generator

Create an **iterator** and subsequent a **generator** that:
-  Takes a list of firstnames, list of lastnames and a number as an input
-  Randomly matches pairs of names
-  Doesn't generate the same pair twice
-  Uses the number for defining the end of the iterator/generator

## Questions