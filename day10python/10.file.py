# FILE I/O-A file is data stored in a storage device. A python program can talk to the file by reading
# content from it and writing content to it.

# There are 2 types of files:
# 1. Text files (.txt, .c, etc)
# 2. Binary files (.jpg, .dat, etc)

import os

# opening a files
f = open("/home/prince/python/data-engineer/day10python/file.txt") #opening a file
data = f.read() #reading a file
print(data) #printing a file
f.close() #closing a file


# READING A FILE IN PYTHON
# Open the file in read mode
f = open("file.txt", "r")
# Read its contents
text = f.read()
# Print its contents
print(text)
# Close the file
f.close()

# WRITE FILES IN PYTHON
# In order to write to a file, we first open it in write or append mode after which, we use
# the python’s f.write() method to write to the file!
# Open the file in write mode
st = "hey boy how are you"

f = open("this.txt", "w")
# Write a string to the file
f.write(st)
# Close the file
f.close()

# f.readline() # Read one line from the file.

f = open('thi.txt')

# readind single lines
line=f.readlines()
print(line,type(line))

# reading multiple lines
line1=f.readlines()
print(line1,type(line1))

line2=f.readlines()
print(line2,type(line2))

line3=f.readlines()
print(line3,type(line3))

line4=f.readlines()
print(line4,type(line4))

line5=f.readlines()
print(line5,type(line5))

# reading files using loop

line=f.readline()
while(line != ""):
    print(line)
    line=f.readline()

f.close()

# WITH STATEMENT-The best way to open and close the file automatically is the with statement.
# Open the file in read mode using 'with', which automatically closes the file
with open("this.txt", "r") as f:
    # Read the contents of the file
    text = f.read()
# Print the contents
print(text)
