#Python - import & modules

Modules are a powerful way to organize and reuse Python code. They can be used to group related functions, classes, and variables together. This makes code more readable, maintainable, and efficient.

To import a module, use the import statement. To import specific functions, classes, and variables from a module, use the from statement.

Once a module is imported, you can access its functions, classes, and variables using the module name followed by a dot (.) and the name of the function, class, or variable.

For example, to import the function add() from the module hello.py, you would use the following statement:

#Python
from hello import add
Use code with caution. Learn more
To call the function add(), you would use the following statement:

#Python
add(1, 2)
Use code with caution. Learn more
Modules can also be imported under a different name. To do this, use the as keyword. For example, to import the module hello.py under the name my_hello, you would use the following statement:

#Python
import hello as my_hello
Use code with caution. Learn more
To call the function add() from the module my_hello, you would use the following statement:

#Python
my_hello.add(1, 2)
