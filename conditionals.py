# If/ Else conditions are used to decide to do something based on something being true or false

x = 3
y = 50

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# IF/ELSE Statement
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')


# IF/IF ELSE/ELSE Statement
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

# NESTED IF STATEMENT
if x > 2:
    if x<=10:
        print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) - Used to combine conditional statements

# AND STATEMENT
if x > 2 and x<=20:
    print(f'{x} is greater than 2 and less than or equal to 20')

# OR STATEMENT
if x > 2 or y > 2:
    print(f'{x} is greater than 2 and {y} greater than 2')

# NOT STATEMENT
if not(x==y):
    print(f'{x} is not equal to {y}')

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object
numbers = [1, 2, 3, 4, 5]

# IN STATEMENT
if x in numbers:
    print(f'{x} in numbers')

# NOT IN STATEMENT
if y not in numbers:
    print(f'{y} not in numbers')

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# IS STATEMENT
x = 50
if x is y:
    print(x is y)

# IS NOT STATEMENT
x = 20
if x is not y:
    print(x is not y)