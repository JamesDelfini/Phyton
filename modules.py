# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager 
# (including Django) as well as custom modules

###################################
## Description: Core Modules
###################################
import datetime
from datetime import date
import time
from time import time

# today = datetime.date.today()
today = date.today()
# timestamp = time.time()
timestamp = time()

print(today, timestamp)


###################################
## Description: Importing Modules third party
# Use pip package manager to install
# pip install camelcase; this will install globally
# pip freeze; will show all the globally installed packages
###################################
# import camelcase
# c = camelcase.CamelCase()
from camelcase import CamelCase
c = CamelCase()
print(c.hump('hello there world'))

###################################
## Description: Import Custom Modules
###################################
import validator
from validator import validate_email

email = 'test@test.com'
if (validate_email(email)):
    print('Email is valid')
else:
    print('Email is invalid')