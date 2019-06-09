# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'James'
age = 22

###################################
## Description: String Formatting
###################################
# Concatenate
print ('Hello, my name is ' + name + ' and I am ' + str(age))

# Arguments by Position
print('My name is {name} and I am {age}'.format(name=name, age=age))

#F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String Methods
s = 'hello world'
sub = 'h'

# Capitalize First Letter in String
print(s.capitalize())

# Make all upercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric without spaces
print(s.isalnum())

# Is all alphabetic without spaces
print(s.isalpha())

# Is all numeric
print(s.isnumeric())