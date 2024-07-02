# 1. Write a python program to display a user entered name followed by Good
# Afternoon using input () function.
# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# 3. Write a program to detect double space in a string.
# 4. Replace the double space from problem 3 with single spaces.
# 5. Write a program to format the following letter using escape sequence
# characters.
# letter = "Dear Prince, this python course is nice. Thanks!"

# q1

name = input("Enter your name: ")
print("Good afternoon",name)
print(f"Good Afternoon {name}")



# q2
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace('<|Name|>','Prince').replace('<|Date|>','20/10/2024'))

# q3
str = "hello bhai how  are you"
print(str.find('  '))

# q4

str = "hello brother how  are you"
print(str.replace("  "," "))

# q5
letter = "Dear Prince,\n\tThis python course is nice.\nThanks!"
print(letter)

print(8)
print(13, end=" ")
print(21)

