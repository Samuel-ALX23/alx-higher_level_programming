ALX Task: 0x05 - Python Exceptions
This task introduces the concept of exceptions in Python. Exceptions are a way of handling errors that occur during the execution of a program. They allow you to gracefully handle errors and continue with the program, rather than crashing the program.

Objectives
The objectives of this task are to:

Understand the concept of exceptions in Python
Learn how to handle exceptions using try-except blocks
Raise custom exceptions
Requirements
You will need to have Python installed on your computer.
You will need to have a basic understanding of Python programming.
Instructions
Create a new file called 0x05-exceptions.py.
Implement the safe_print_list function as described in the task instructions.
Test your code by writing a main function that calls the safe_print_list function with different values of my_list and x.
Example Usage
The following example shows how to use the safe_print_list function:

Python
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
Use code with caution. Learn more
This code will print the following output:

12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
Additional Notes
You can use the try-except block to handle multiple exceptions.
You can raise custom exceptions using the raise keyword.
