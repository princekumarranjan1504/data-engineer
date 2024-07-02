# Dictionary is a collection of keys-value pairs.
# Syntax:
a = {
"key": "value",
"harry": "code",
"marks": "100",
"list": [1, 2, 9]
}
print(a["key"]) # Output: "value"
print(a["list"]) # Output: [1, 2, 9]

# DICTIONARY METHODS
# Consider the following dictionary.

b = {"name": "prince",
     "from": "india",
     "marks": [92,98,96]
     }

b.items() # Returns a list of (key,value)tuples.
b.keys() #Returns a list containing dictionary's keys.
b.update({"friends"}) #Updates the dictionary with supplied key-value pairs.
b.get("name") #Returns the value of the specified keys (and value is returned eg."prince" is returned here).

# SETS IN PYTHON.
# Set is a collection of non-repetitive elements.
s = set() # no repetition allowed!
s.add(1)
s.add(2) # or set ={1,2}

# OPERATIONS ON SETS
# Consider the following set:
s = {1,8,2,3}
len(s) #Returns 4, the length of the set
s.remove(8) #Updates the set s and removes 8 from s.
s.pop() #Removes an arbitrary element from the set and return the element removed.
s.clear() #empties the set s.
s.union({8,11}) #Returns a new set with all items from both sets. {1,8,2,3,11}.
s.intersection({8,11}) # Return a set which contains only item in both sets {8}.