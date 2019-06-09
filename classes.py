# A class is like a blueprint for creating objects. 
# An object has properties and methods(functions) associated with it. 
# Almost everything in Python is an object

###################################
## Description: Create Class
###################################
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    def has_birthday(self):
        self.age += 1

# Init User Object
james = User('James Delfini', 'sauer@gmail.com', 22)

print(type(james))
print(james.age)
james.has_birthday()
print(james.age)
print(james.greeting())

###################################
## Description: Extend Class
###################################
class Customer(User):
        # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

hazel = Customer('Hazel Nornea', 'hazel@gmail.com', '21')
hazel.set_balance(500)
print(hazel.greeting())