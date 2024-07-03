# print 1 to 10 
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# the same task can be done by loops
for i in range (1, 11):
    print(i)

# types of loops
# 1.while 
# 2.for

i=1
while(i<6): # The block keeps executing until the condition is true
    print(i)
    i +=1

# Quick Quiz: Write a program to print 1 to 50 using a while loop.
i=1
while(i<51): # The block keeps executing until the condition is true
    print(i)
    i +=1

# Quick Quiz: Write a program to print the content of a list using while loops.
li = [1,2,3,4,'prince','hello',False]
i=0
while(i<len(li)):
    print(li[i])
    i +=1

# for loop
for i in range(51):
    print(i)

# Quick Quiz: Write a program to print the content of a list using for loops.
li = [1,2,3,4,'prince','hello',False]
for item in li:
    print(item)

# for loop iterate tuple
t=(1,2,3,4,5)
for i in t:
    print(i)

# for loop to iterate string
str='prince'
for i in str:
    print(i)

# range() function step size
# print 1 to 50 with stepping 4
for i in range(0,51,4):
    print(i)

# FOR LOOP WITH ELSE

l=[1,3,4,5,6]
for i in l:
    print(i)
else:
    print("done")


# THE BREAK STATEMENT
for i in range(100):
    print(i)
    if(i==5):
        break #exit the loop right now

# THE CONTINUE STATEMENT
for i in range(100):
    if(i==10):
        continue #skip this iteration
    print(i)

# PASS STATEMENT
for i in range(100):
    pass  # without pass, the program will throw an error

i=0
while(i<10):
    print(i)
    i+=1