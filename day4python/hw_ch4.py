# 1. Write a program to store seven fruits in a list entered by the user.
# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
# 3. Check that a tuple type cannot be changed in python.
# 4. Write a program to sum a list with 4 numbers.
# 5. Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)

# q1
fruits = []
f1=input("1")
fruits.append(f1)
f2=input("2")
fruits.append(f2)
f3=input("3")
fruits.append(f3)
f4=input("4")
fruits.append(f4)
f5=input("5")
fruits.append(f5)
f6=input("6")
fruits.append(f6)
f7=input("7")
fruits.append(f7)
print(fruits)

# q2
marks=[]
s1=int(input("m1"))
marks.append(s1)
s2=int(input("m2"))
marks.append(s2)
s3=int(input("m3"))
marks.append(s3)
s4=int(input("m4"))
marks.append(s4)
s5=int(input("m5"))
marks.append(s5)
s6=int(input("m6"))
marks.append(s6)
marks.sort()
print(marks)

# q3
t=(1,2,3,'a','b')
t[2]="c"
print(t)

# q5
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))

# q4
l=[3,4,2,5]
print(sum(l))