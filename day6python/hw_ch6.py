# 1. Write a program to find the greatest of four numbers entered by the user.
# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
# 4. Write a program to find whether a given username contains less than 10 characters or not.
# 5. Write a program which finds out whether a given name is present in a list or not.
# 6. Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50=> F
# 7. Write a program to find out whether a given post is talking about “Harry” or not.



# q1
num1=int(input('1:'))
num2=int(input('2:'))
num3=int(input('3:'))
num4=int(input('4:'))

if(num1>num2 and num1>num3 and num1>num4):
    print('num1 is greater:',num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print('num2 is greater:',num2)
elif(num3>num1 and num3>num2 and num3>num4):
    print('num3 is greater:',num3)
else:
    print('num4 is greater:',num4)

# q2

marks1=(int(input('enter 1 marks:')))
marks2=(int(input('enter 2 marks:')))
marks3=(int(input('enter 3 marks:')))
totalMarks=(marks1+marks2+marks3)
percentage=(totalMarks/300)*100
print(totalMarks,percentage)

if(percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print('pass')
else:
    print('fail')

# q4
username=input()
length=len(username)
if(length<10):
    print(True)
else:
    print(False)

# q6
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

# q3
p1='Make a lot of money' 
p2='buy now' 
p3='subscribe this' 
p4='click this'
message=input('enter your comment: ')
if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("Spam")
else:
    print('not Spam')

# q5
l=['prince','sonu','babu','baby']
name=input("enter your name:")
if(name in l):
    print('your name is in the list')
else:
    print('you are not in the list')


# q7
post=input('enter your post:')
if('Harry'.lower() in post.lower()):
    print('post is talking about harry')
else:
    print('not talking about harry')
