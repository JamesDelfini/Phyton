# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

###################################
## Description: Create Dictionary
###################################
# Create key value pairs; like JSON or Objects in JavaScript
person = {
    'first_name': 'Sauer',
    'last_name': 'Voussoir',
    'age': 30
}

# Use constructor
person2 = dict(first_name='James', last_name='Delfini')

print(person, type(person))
print(person2, type(person2))

# Get a value in position
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-5555-555'
print(person)

# Get dictionaries keys Keys()
print(person.keys())

# Get dictionaries items Items()
print(person.items())

#Copy dictioanry Copy(); Spread Operator in JavaScript
person3 = person.copy()
person3['city'] = 'Boston'

print(person3)

# Remove an Item Del() & Pop()
del(person['age'])
person.pop('phone')
print(person)

# Clear dictionary Clear()
person.clear()
print(person)

# Get Length
print(len(person3))

# List of Dictionary
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)

# Get a list of dictionary position
print(people[1]['name'])