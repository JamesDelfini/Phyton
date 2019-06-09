# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

###################################
## Description: For Loop
###################################
people = ['Sarah', 'Susan', 'Hazel', 'John', 'Paul']

# for person in people:
#     print(f'Current person: {person}')

# Break Loop Statement
# for person in people:
#     if person == 'Hazel':
#         break
#     print(f'Current person: {person}')

# Continue Loop Statement
# for person in people:
#     if person == 'Hazel':
#         continue
#     print(f'Current person: {person}')

# Range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')
# Number: 1 ... Number: 2 .. Number: 10(i)


# While loops execute a set of statements as long as a condition is true.

###################################
## Description: Create White Loop
###################################
count = 0 
while count<=10:
    print(f'Count: {count}')
    count +=1
# Count: 1 ... Count: 2 ... Count: 10(count)