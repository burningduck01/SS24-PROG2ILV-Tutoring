# Session 2

## exercise 1: Sockets

In the exercise1 folder is already an exercise.py file defined, that if you want to use it, creates a **Server** object and executes the `run()` method in another thread. A **Client** object is also started by executing the `run()` method.

### Part 1: Sockets
Create a TCP client server connection, enabeling the client sending a message to the server and printing the recieved massage in the server console.

### Part 2: Threading
Implement a multithreaded implimentation on the server side. Think of accepting in a loop and running the connection in another **Thread**. What are the different ways to implement multithreading?

### Part 3: OOP
Create a message **Class**, that stores a **username** and **message**. Implement a method to enable sending these attributes to the server in one message. On the server use a **classmethode** to recreate the message object, then print the sent message with the username in square brackets in the front. Therefore decide on a way to separate these attributes in the exported message, that your are sending between server and client.

### Part 4: Interactivity
Sending message objects to the server and return a random one of a set of predefined answer messages. On client side, at the start, ask for the **server address**, **username** and **each** time for the **message** you want to send.

### Part 4: Testing
Write test cases, test each:
- server and client connection
- message object
- interactivity