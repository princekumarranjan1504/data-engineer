# We can primarily write a string in these three ways.
a ='harry' # Single quoted string
b = "harry" # Double quoted string
c = '''harry''' # Triple quoted string

# String Slicing
str = 'Prince'
print(str[0:2])
print(str[-4:-1])


# slicing with skip values
word = "amazing"
word[1: 6: 2] # "mzn"

# Other advanced slicing techniques:

Word = "amazing"
Word[:7] # word [0:7] – 'amazing'
Word[0:] # word [0:7] – 'amazing'

# String function 
# 1. len () function – This function returns the length of the strings.
str = "harry"
print(len(str)) # Output: 5

# 2. String.endswith("rry") – This function_ tells whether the variable string ends with
# the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends with rry.
str = "harry"
print(str.endswith("rry")) # Output: True

# 3. string.count("c") – counts the total number of occurrences of any character.
str = "harry"
count = str.count("r")
print(count) # Output: 2

# 4. the first character of a given string.
str = "harry"
capitalized_string = str.capitalize()
print(capitalized_string) # Output: "Harry"

# 5. string.find(word) – This function friends a word and returns the index of first
# occurrence of that word in the string.
str = "harry"
index = str.find("rr")
print(index) # Output: 2

# 6. string.replace (old word, new word ) – This function replace the old word with
# new word in the entire string.
str = "harry"
replaced_string = str.replace("r", "l")
print(replaced_string) # Output: "hally"
