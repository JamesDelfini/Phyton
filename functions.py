# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

###################################
## Description: Create Function
###################################
def sayHello(name='Delfini'):
    print(f'Hello {name}')


sayHello('James')
sayHello()

# Return a Value in Function 
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(3, 4)
print(num)
num += 3
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

###################################
## Description: Create Lambda Function
###################################
getSum2 = lambda num1, num2: num1 + num2

print(getSum2(10, 3))