# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
# 2. Write a program to input eight numbers from the user and display all the uniquenumbers (once).
# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

# 5. s = {}
# What is the type of 's'?
# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
# 8. If languages of two friends are same; what will happen to the program in problem 6?
# 9. Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]}

# q1
d = {
    'madad':'help',
    'kursi':'chair',
    'billi':'cat'
}

d1=input('enter the word you want meaning of:')

print(d[d1],type(d))

# q2
s=set()
s.add(int(input('first no:')))
s.add(int(input('second no:')))
s.add(int(input('third no:')))
s.add(int(input('fouth no:')))
s.add(int(input('fifth no:')))
s.add(int(input('sixth no:')))
s.add(int(input('seventh no:')))
s.add(int(input('eighth no:')))
print(s,type(s))

# q3
s=set()
s.add(18)
s.add('18')
print(s)

# q4
s = set()
print(s)
s.add(20)
print(s)
s.add(20.0)
print(s,'2')
s.add('20')
print(s,'3')
print(len(s))

# q5
s={}
print(type(s))

# q6
d={}
d.update({input("name 1:"):input("fav fruits:")})
d.update({input("name 2:"):input("fav fruits:")})
d.update({input("name 3:"):input("fav fruits:")})
d.update({input("name 4:"):input("fav fruits:")})
print(d),type(d)

# q7
# if the name of two friends are same then it  pick last update key of the name

# q8
# if the fruits are same of 2 friends then it return rhe values of the keys

# q9
s = {8, 7, 12, "Harry", [1,2]}
print(s,type(s))
# we can not list the inside the set and set is hashable and immutable