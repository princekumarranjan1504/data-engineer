# 1. Write a program using functions to find greatest of three numbers.
# 2. Write a python program using function to convert Celsius to Fahrenheit.
# 3. How do you prevent a python print() function to print a new line at the end.
# 4. Write a recursive function to calculate the sum of first n natural numbers.
# 5. Write a python function to print first n lines of the following pattern:
'''
***
**   - for n = 3
*   
'''
# 6. Write a python function which converts inches to cms.
# 7. Write a python function to remove a given word from a list ad strip it at the same time.
# 8. Write a python function to print multiplication table of a given number.

# q1
def greaterst_number(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    return

n=greaterst_number(10,6,4)
print(n)


# # q2
def tempF(c):
    return (c*9/5)+32

celcius = int(input('enter the celcius Temperature'))
print(f'the fahrenhiet temperature is: {tempF(celcius)}')

# q3
# def print():
#     print(end="")


# q4
def sumOf(n):
    if(n==1):
        return 1
    return sumOf(n-1)+n

sum=int(input('enter the number:'))
print(f'Sum of number is: {sumOf(sum)}')

# q5
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
    
pattern(5)

# q6
def cms(n):
    return n*2.54

inch = int(input('enter inch:'))
print(f'centimeter is: {cms(inch)}')

# q7
def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l=['prince','rohan','shubham','an']
print(rem(l,'an'))


# q8
def table(n):
    for i in range(1,11):
        print(f"{n}X{i}={n*(i)}")
    return "done"

n=int(input('enter the number:'))
print(table(n))

