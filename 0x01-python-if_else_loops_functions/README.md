# Python - if/else, loops, functions
This README file provides a brief overview of if/else statements, loops, and functions in Python.

if/else statements
if/else statements are conditional statements that allow you to check if a condition is true and execute a block of code if it is. If the condition is false, you can execute a different block of code.

The basic syntax for an if/else statement is as follows:

#Python
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
Use code with caution. Learn more
For example, the following code checks if the variable age is greater than 18. If it is, the code prints the message "You are an adult" to the console. Otherwise, the code prints the message "You are not an adult" to the console.

#Python
age = 19

if age > 18:
    print("You are an adult")
else:
    print("You are not an adult")
Use code with caution. Learn more
loops
Loops allow you to execute a block of code multiple times. There are two main types of loops in Python: for loops and while loops.

for loops

For loops allow you to iterate over a sequence of items. The basic syntax for a for loop is as follows:

#Python
for item in sequence:
    # code to execute for each item in the sequence
Use code with caution. Learn more
For example, the following code prints each number from 1 to 10 to the console:

#Python
for i in range(1, 11):
    print(i)
Use code with caution. Learn more
while loops

While loops allow you to execute a block of code while a condition is true. The basic syntax for a while loop is as follows:

#Python
while condition:
    # code to execute while condition is true
Use code with caution. Learn more
For example, the following code prints the number 1 to the console and then increments the number by 1 until the number is equal to 10.

#Python
i = 1

while i < 10:
    print(i)
    i += 1
Use code with caution. Learn more
#functions
Functions allow you to group related code together and reuse it throughout your program. Functions can also accept parameters and return values.

The basic syntax for a function definition is as follows:

#Python
def function_name(parameters):
    # code to execute when the function is called
    return value
Use code with caution. Learn more
For example, the following function definition defines a function that takes two numbers as parameters and returns the sum of those numbers.

#Python
def add_two_numbers(a, b):
    return a + b
Use code with caution. Learn more
The function can then be called as follows:

#Python
sum = add_two_numbers(10, 20)
print(sum)
Use code with caution. Learn more
This will print the number 30 to the console.

#Conclusion
if/else statements, loops, and functions are three fundamental programming concepts that are essential for writing Python programs. By understanding and using these concepts effectively, you can write more powerful and efficient code.
