# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

###################################
## Description: Create tuples
###################################
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes')) # Constructor
print(fruits, fruits2)
print(type(fruits2))

# A string without trailing comma
fruits2 = ('Apples')
print(fruits2)
print(type(fruits2))

# A tuple requires a trailing comma to be considered as a collection.
fruits2 = ('Apples',)
print(fruits2)
print(type(fruits2))

# Get value
print(fruits[1])

# Can't change a value
# fruits2[0] = 'Pears' # TypeError: 'tuple' object does not support item assignment

# Delete tuple
del fruits2
# print(fruits2) #NameError: name 'fruits2' is not defined

# Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.
