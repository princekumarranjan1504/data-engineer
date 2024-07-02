# 1. Write a python program to add two numbers.
# 2. Write a python program to find remainder when a number is divided by z.
# 3. Check the type of variable assigned using input () function.
# 4. Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80
# 5. Write a python program to find an average of two numbers entered by the user.
# 6. Write a python program to calculate the square of a number entered by the user.

#q1.
a = 1 
b=2
print(a+b)

#q2
a = int(input())
b = int(input())
print(a//b)

# q3
a=input()
b=type(a)
print(b)

# q4
a=int(input("1: "))
b=int(input("2: "))
print("a is greater than b is ", a>b)

# q5
a=int(input("enter 1 no. "))
b=int(input("enter 2 no. "))
print("avg no is ",(a+b)/2)

# # q6
a=int(input("enter no "))
print("sq of thre no is ",a*a)