CHAPTER 7 – LOOPS IN PYTHON

Sometimes we want to repeat a set of statements in our program. For instance: Print 1
to 1000.
Loops make it easy for a programmer to tell the computer which set of instructions to
repeat and how!

TYPES OF LOOPS IN PYTHON
Primarily there are two types of loops in python.
while loops
for loops
We will look into these one by one.

WHILE LOOP
Syntax:
while (condition): # The block keeps executing until the condition is true
    #Body of the loop

In while loops, the condition is checked first. If it evaluates to true, the body of the loop is executed otherwise not!
If the loop is entered, the process of [condition check & execution] is continued until the condition becomes False.

Quick Quiz: Write a program to print 1 to 50 using a while loop.
i=1
while(i<51): # The block keeps executing until the condition is true
    print(i)
    i +=1

Example:
i = 0
while i < 5: # print "prince" – 5 times!
    print("prince")
i = i + 1

Note: If the condition never become false, the loop keeps getting executed.

Quick Quiz: Write a program to print the content of a list using while loops.
li = [1,2,3,4,'prince','hello',False]
i=0
while(i<len(li)):
    print(li[i])
    i += 1

FOR LOOP
A for loop is used to iterate through a sequence like list, tuple, or string [iterables]

Syntax:
l = [1, 7, 8]
for item in l:
    print(item) # prints 1, 7 and 8

RANGE FUNCTION IN PYTHON
The range() function in python is used to generate a sequence of number.
We can also specify the start, stop and step-size as follows:

range(start, stop, step_size) # step_size is usually not used with range()

AN EXAMPLE DEMONSTRATING RANGE () FUNCTION.
for i in range(0,7): # range(7) can also be used.

print(i) # prints 0 to 6
FOR LOOP WITH ELSE
An optional else can be used with a for loop if the code is to be executed when the loops exhausts.

Example:
l= [1,7,8]
for item in l:
    print(item)
else:
    print("done") # this is printed when the loop exhausts!

Output:
1
7
8
done

THE BREAK STATEMENT
‘break’ is used to come out of the loop when encountered. It instructs the program to –
exit the loop now.

Example:
for i in range (0,80):
    print(i) # this will print 0,1,2 and 3
    if i==3
        break

THE CONTINUE STATEMENT
‘continue’ is used to stop the current iteration of the loop and continue with the next
one. It instructs the Program to “skip this iteration”.
Example:
for i in range(4):
    print("printing")
    if i == 2: # if i is 2, the iteration is skipped
        continue
    print(i)

PASS STATEMENT
pass is a null statement in python.
It instructs to “do nothing”.

Example:
l = [1,7,8]
for item in l:
    pass # without pass, the program will throw an error