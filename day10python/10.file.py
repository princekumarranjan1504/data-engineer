# FILE I/O-A file is data stored in a storage device. A python program can talk to the file by reading
# content from it and writing content to it.

# There are 2 types of files:
# 1. Text files (.txt, .c, etc)
# 2. Binary files (.jpg, .dat, etc)

# opening a files
f=open("file.txt") #opening a file
data = f.read() #reading a file
print(data) #printing a file
f.close() #closing a file

