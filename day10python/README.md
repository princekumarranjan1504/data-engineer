CHAPTER 9 – FILE I/O

The random-access memory is volatile, and all its contents are lost once a program
terminates. In order to persist the data forever, we use files.
A file is data stored in a storage device. A python program can talk to the file by reading
content from it and writing content to it.

TYPE OF FILES.
There are 2 types of files:
1. Text files (.txt, .c, etc)
2. Binary files (.jpg, .dat, etc)
Python has a lot of functions for reading, updating, and deleting files.

OPENING A FILE
Python has an open() function for opening files. It takes 2 parameters: filename and
mode.
# open("filename", "mode of opening(read mode by default)")
open("this.txt", "r")

READING A FILE IN PYTHON
# Open the file in read mode
f = open("this.txt", "r")
# Read its contents
text = f.read()
# Print its contents
print(text)
35# Close the file
f.close()

OTHER METHODS TO READ THE FILE.
We can also use f.readline() function to read one full line at a time.
f.readline() # Read one line from the file.
MODES OF OPENING A FILE
r – open for reading
w - open for writing
a - open for appending
+ - open for updating.
‘rb’ will open for read in binary mode.
‘rt’ will open for read in text mode.

WRITE FILES IN PYTHON
In order to write to a file, we first open it in write or append mode after which, we use
the python’s f.write() method to write to the file!
# Open the file in write mode
f = open("this.txt", "w")
# Write a string to the file
f.write("this is nice")
# Close the file
f.close()

WITH STATEMENT
The best way to open and close the file automatically is the with statement.
# Open the file in read mode using 'with', which automatically closes the
file
with open("this.txt", "r") as f:
# Read the contents of the file
text = f.read()
# Print the contents
print(text)