# Python has functions for creating, reading, updating, and deleting files.

###################################
## Description: Create File
# File created is "myfile.txt"
###################################

# Open a File
myFile = open('myfile.txt', 'w') # w - for write

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to File
myFile.write('Python rocks!')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a') # a - append to the file
myFile.write('. PHP also rocks! YEEEAH!')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+') # r+ - reading the file
text = myFile.read(100)
print(text)