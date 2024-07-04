# FUNCTIONS:A function is a group of statements performing a specific task.

def func():
    print('hello')

# average function 
def avg(): #function defination
    a=int(input('enter 1st no:'))
    b=int(input('enter 2nd no:'))
    c=int(input('enter 3rd no:'))
    avg=(a+b+c)/2
    print(avg)

avg() #function call to execute function

# Quick Quiz: Write a program to greet a user with “Good day” using functions.

def greet():
    print("Good Day!")

greet()

# TYPES OF FUNCTIONS IN PYTHON

# There are two types of functions in python:
# Built in functions (Already present in python)
# User defined functions (Defined by the user)

# Examples of built in functions includes len(), print(), range() etc.
# The func1() function we defined is an example of user defined function.

# FUNCTIONS WITH ARGUMENTS

def greet(name,ending):
    print("Good Day!,"+name)
    print(ending)

greet("Prince","hii")
greet("Harshit","bye")

# function return values

def greet(name,ending):
    print("Good Day!,"+name)
    print(ending)
    return 'Done'

a=greet("Prince","hii")
print(a)

# avg()

def average(a,b,c):
    avg=(a+b+c)/2
    return avg

avg = average(5,3,4)
print(avg)


# DEFAULT PARAMETER VALUE:We can have a value as default as default argument in a function.

def greet(name,ending="Thanks"):
    print(f"Good Day! {name}")
    print(ending)

greet("Prince")


# RECURSION:Recursion is a function which calls itself.
'''
factorial(0)=1
factorial(1)=1
factorial(2)=1 X 2 
factorial(5)=1 X 2 X 3 
factorial(4)=1 X 2 X 3 X 4 
factorial(5)=1 X 2 X 3 X 4 X 5

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

factorial(n)=n X n-1 X n-2 X ... X 3 X 2 X 1
factorial(n)=n X factorial(n-1) ---> general formula
'''


def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n=int(input("Enter a number:"))
print(f"The factorial of this number is : {factorial(n)}")