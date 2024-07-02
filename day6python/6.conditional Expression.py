# Syntax:
# if (condition1): # if condition1 is True
#     print ("yes")
# elif(condition2): # if condition2 is True
#     print("no")
# else: # otherwise
#     print("maybe")

# CODE EXAMPLE.
a=22
if(a>9):
    print("greater")
else:
    print("lesser")

# Quick Quiz: Write a program to print yes when the age entered by the user is greater
# than or equal to 18.

age = int(input('Enter you age: '))

if(age>=18):
    print('yes')
else:
    print('no')

# ELIF CLAUSE SYNTAX:
# elif in python means [else if]. An if statements can be chained together with a lot of these elif statements followed by an else statement.

# if (condition1):
#     #code
# elif (condition2): # this ladder will stop once a condition in an if or elif is met.
#     #code
# elif(condition3):
#     #code
# else:
#     #code

# Write a program to calculate the grade of a student from his marks from the following scheme

marks = int(input('enter your marks:'))
if(marks>100):
    print('invalid marks')
elif(marks>=90):
    print('Grade Ex')
elif(marks>=80):
    print('Grade A')
elif(marks>=70):
    print('grade B')
elif(marks>=60):
    print('Grade C')
elif(marks>=50):
    print('Grade D')
else:
    print('Grade F')