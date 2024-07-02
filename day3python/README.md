CHAPTER 3 – STRINGS

String is a data type in python.
String is a sequence of characters enclosed in quotes.
We can primarily write a string in these three ways.

a ='harry' # Single quoted string
b = "harry" # Double quoted string
c = '''harry''' # Triple quoted string


STRING SLICING

A string in python can be sliced for getting a part of the strings.
Consider the following string:

Name="Prince"=>Length=6
indexing start from 0 1 2 3 4 5 6 i.e 0 to (len-1)

The index in a sting starts from 0 to (length -1) in Python. In order to slice a string, we use the following syntax:

sl=name[index_start:index_end]
sl[0:3] returns 'Pri'--->characters from 0 to 3 it means it return upto 2
sl[1:3] returns 'ri'---->characters from 1 to 3 it means it return upto 2

Negative Indices: Negative indices can also be used as shown in the figure above. -1 corresponds to the (length - 1) index, -2 to (length - 2).

indexing starts from -6 -5 -4 -3 -2 -1 

SLICING WITH SKIP VALUE

We can provide a skip value as a part of our slice like this:
word = "amazing"
word[1: 6: 2] # "mzn"

Other advanced slicing techniques:

Word = "amazing"
Word = [:7] # word [0:7] – 'amazing'
Word = [0:] # word [0:7] – 'amazing'

STRING FUNCTIONS

Some of the commonly used functions to perform operations on or manipulate strings
are as follows. Let us assume there is a string ‘str’ as follows:
str = 'harry'

Now when operated on this string ‘str’, these functions do the following:
1. len () function – This function returns the length of the strings.
str = "harry"
print(len(str)) # Output: 5

2. String.endswith("rry") – This function_ tells whether the variable string ends with
the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends
with rry.
str = "harry"
print(str.endswith("rry")) # Output: True

3. string.count("c") – counts the total number of occurrences of any character.
str = "harry"
count = str.count("r")
print(count) # Output: 2

4. the first character of a given string.
str = "harry"
capitalized_string = str.capitalize()
print(capitalized_string) # Output: "Harry"

5. string.find(word) – This function friends a word and returns the index of first
occurrence of that word in the string.
str = "harry"
index = str.find("rr")
print(index) # Output: 2

6. string.replace (old word, new word ) – This function replace the old word with
new word in the entire string.
str = "harry"
replaced_string = str.replace("r", "l")
print(replaced_string) # Output: "hally"

ESCAPE SEQUENCE CHARACTERS

Sequence of characters after backslash "\" → Escape Sequence characters
Escape Sequence characters comprise of more than one character but represent one character when used within the strings.

Example:
\n --> newline
\t --> tab
\' --> Singleqote
\\ --> backslash
etc.