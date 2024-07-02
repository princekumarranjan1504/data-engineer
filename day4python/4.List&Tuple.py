# creating list
friends=["apple","akash","rohan",7,False]
print(friends)

# LIST INDEXING

l1 = [7,9,"harry"]
l1[0] # 7
l1[1] # 9
l1[70] # error
l1[0:2] # [7,9] #list slicing

# List methods

l1 = [1,8,7,2,21,15]

l1.sort() # updates the list to [1,2,7,8,15,21]
l1.reverse() # updates the list to [15,21,2,7,8,1]
l1.append(8) # adds 8 at the end of the list
l1.insert(3,8) # This will add 8 at 3 index
l1.pop(2) # Will delete element at index 2 and return its value.
l1.remove(21) # Will remove 21 from the list.

# A tuple is an immutable data type in python.
a = () # empty tuple
a = (1,) # tuple with only one element needs a comma
a = (1,7,2) # tuple with more than one element

# tuple methods

a = (1, 7, 2)
a.count (1) # a count (1) will return number of times 1 occurs in a.
a.index (1) #will return the index of first occurrence of 1 in a.