# 1. Write a program to print multiplication table of a given number using for loop.
# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# 3. Attempt problem 1 using while loop.
# 4. Write a program to find whether a given number is prime or not.
# 5. Write a program to find the sum of first n natural numbers using while loop.
# 6. Write a program to calculate the factorial of a given number using for loop.
'''7. Write a program to print the following star pattern.
*
***
***** for n = 3'''
'''8. Write a program to print the following star pattern:
*
**
*** for n = 3'''
'''9. Write a program to print the following star pattern.
***
* * for n = 3
***'''
# 10. Write a program to print multiplication table of n using for loops in reversed
# order.

# # q1
a=int(input())
for i in range(1,11):
    print(f"{a}X{i}={a*i}")

# q2
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if(name.startwith("S")):
        print(f"Hello {name}")

# q3
a=int(input())
i=1
while(i<11):
    print(a*i)
    i+=1

# q4
n=int(input())
for i in range(2,n):
    if(n%i)==0:
        print("Number is not Prime")
        break
else:
    print("Number is Prime")


# q5
n=int(input())
sum=0
i=1
while(i<=n):
    sum+=i
    i+=1
print(sum)

# q6
f=int(input())
fact=1
for i in range(1,f+1):
    fact *= i
print(fact)

# q7
n=int(input())
for i in range(1,n+1):
    print(" "* (n-i), end="")
    print("*"*( 2*i-1), end="")
    print("")

# q8
n=int(input())
for i in range(1,n+1):
    # print(" "* (n-1), end="")
    print("*"* (i), end="")
    print("")

# q9
n=int(input())
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2),end="")
        print("*", end="")
    print("")

# q10
a=int(input())
for i in range(1,11):
    print(f"{a}X{11-i}={a*(11-i)}")