CHAPTER 6 – CONDITIONAL EXPRESSION

Sometimes we want to play PUBG on our phone if the day is Sunday.
Sometimes we order Ice Cream online if the day is sunny.
Sometimes we go hiking if our parents allow.
All these are decisions which depend on a condition being met.
In python programming too, we must be able to execute instructions on a condition(s)
being met.
This is what conditionals are for!


IF ELSE AND ELIF IN PYTHON
If else and elif statements are a multiway decision taken by our program due to certain
conditions in our code.

Syntax:
if (condition1): # if condition1 is True
    print ("yes")
elif(condition2): # if condition2 is True
    print("no")
else: # otherwise
    print("maybe")

CODE EXAMPLE.
a=22
if(a>9):
    print("greater")
else:
    print("lesser")

Quick Quiz: Write a program to print yes when the age entered by the user is greater than or equal to 18.

age = int(input('Enter you age: '))

if(age>=18):
    print('yes')
else:
    print('no')

RELATIONAL OPERATORS
Relational Operators are used to evaluate conditions inside the if statements. Some examples of relational operators are:
==: equals.
> =: greater than/ equal to.
< =: lesser than/ equal to.

LOGICAL OPERATORS
In python logical operators operate on conditional statements. For Example:
and – true if both operands are true else false.
or – true if at least one operand is true or else false.
not – inverts true to false & false to true.

ELIF CLAUSE
elif in python means [else if]. An if statements can be chained together with a lot of these elif statements followed by an else statement.

if (condition1):
    #code
elif (condition2): # this ladder will stop once a condition in an if or elif is met.
    #code
elif(condition3):
    #code
else:
    #code

IMPORTANT NOTES:
1. There can be any number of elif statements.
2. Last else is executed only if all the conditions inside elifs fail.