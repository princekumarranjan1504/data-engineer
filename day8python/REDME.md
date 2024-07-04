CHAPTER 8 – FUNCTIONS & RECURSIONS

A function is a group of statements performing a specific task.
When a program gets bigger in size and its complexity grows, it gets difficult for a
program to keep track on which piece of code is doing what!
A function can be reused by the programmer in a given program any number of

EXAMPLE AND SYNTAX OF A FUNCTION

The syntax of a function looks as follows:
def func1():
print('hello')
This function can be called any number of times, anywhere in the program.

FUNCTION CALL

Whenever we want to call a function, we put the name of the function followed by
parentheses as follows:
func1() # This is called function call.

FUNCTION DEFINITION

The part containing the exact set of instructions which are executed during the function
call.

Quick Quiz: Write a program to greet a user with “Good day” using functions.
def greet():
    print("Good Day!")
greet()

TYPES OF FUNCTIONS IN PYTHON

There are two types of functions in python:
Built in functions (Already present in python)
User defined functions (Defined by the user)
Examples of built in functions includes len(), print(), range() etc.
The func1() function we defined is an example of user defined function.

FUNCTIONS WITH ARGUMENTS

A function can accept some value it can work with. We can put these values in the
parentheses.

A function can also return value as shown below:
30def greet(name):
gr = "hello"+ name
return gr
a = greet ("harry")
# a will now contain "hello harry"

DEFAULT PARAMETER VALUE

We can have a value as default as default argument in a function.
If we specify name = “stranger” in the line containing def, this value is used when no
argument is passed.
Example:
def greet(name = "stranger"):
# function body

greet() # name will be "stranger" in function body (default)
greet("harry") # name will be "harry" in function body (passed)

RECURSION

Recursion is a function which calls itself.
It is used to directly use a mathematical formula as function.
Example:
factorial(n) = n x factorial (n-1)

This function can be defined as follows:
def factorial(n)
if i == 0 or i==1: # base condition which doesn’t call the function
any further
return 1
else:
return n*factorial(n-1) # function calling itself

31This works as follows:
Factorial(5)
 /    \
5XFactorial(4)
   /    \
5X4XFactorial(3)
     /     \
5X4X3XFactorial(2)
       /    \
5X4X3X2XFactorial(1)
         /
5X4X3X2X1

The programmer needs to be extremely careful while working with recursion to ensure
that the function doesn’t infinitely keep calling itself. Recursion is sometimes the most
direct way to code an algorithm.