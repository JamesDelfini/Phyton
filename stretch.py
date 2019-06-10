## 10 Python Tips and Tricks For Writing Better Code
# https://www.youtube.com/watch?v=C-gEQdGVXbk

# 1. Ternary Conditionals aka inline if statement
isValidated = True
myVar = 777 if isValidated else 666

print(myVar)

# 2. Underscore Placeholders
# To make the code readable
num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(f'{total:,}')
# 10,100,000,000

# 3. Context Managers
with open('myfile.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)

# 4. Enumerate using Enumerate(<list>, [start=(n)])
names = ['Corey', 'Chris', 'Dave', 'Travis']
for index, name in enumerate(names, start=1):
    print(index, name)
# 1 Corey
# 2 Chris
# 3 Dave
# 4 Travi

# 5. Zip(<list>, <list>, ...)
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']
for name, hero, universe in zip(names, heroes, universes): # Unpacking
    print(f'{name} is actually {hero} from {universe}') # Outputs a Tuple
# Peter Parker is actually Spiderman from Marvel
# Clark Kent is actually Superman from DC
# Wade Wilson is actually Deadpool from Marvel
# Bruce Wayne is actually Batman from DC

# Use Zip Longest Function from Aether Tools Module for unbalanced list
for value in zip(names, heroes, universes): # Packing
    print(value) # Outputs a Tuple
# ('Peter Parker', 'Spiderman', 'Marvel')
# ('Clark Kent', 'Superman', 'DC')
# ('Wade Wilson', 'Deadpool', 'Marvel')
# ('Bruce Wayne', 'Batman', 'DC')

# 6. Unpacking
# Normal
items = (1, 2)
print(items)

# Unpacking
a, _ = (1, 2) # Use "_" for the variable will not be used 
a, b, *c = (1, 2, 3, 4, 5) # Use "*" to unpack inside the variable
a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
print(a)
print(b)
print(c)
print(d)

# 7. Setattr/Getattr