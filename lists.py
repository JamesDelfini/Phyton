# A List is a collection which is ordered and changeable. Allows duplicate members.

###################################
## Description: Create list
###################################
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a Constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2, fruits)
print(fruits[1], len(fruits[1]))

# Append to list
fruits.append('Mango')
print(fruits)

# Remove from list
fruits.remove('Grapes')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Change Value
fruits[0] = 'Blueberries'

# Remove with Pop()
fruits.pop(2)
print(fruits)

# Reverse list Reverse()
fruits.reverse()
print(fruits)

# Sort List Sort()
fruits.sort()
print(fruits)

# Reverse Sort Sort(reserve=<Boolean>)
fruits.sort(reverse=True)
print(fruits)