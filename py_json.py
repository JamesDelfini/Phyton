# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

###################################
## Description: Deserialize JSON
###################################
userJSON = '{"first_name": "Hazel", "last_name": "Nornea", "age": 21}'

# Parse to Dictionary. It is like JSON.parse(<JSON_DATA>) in JavaScript
user = json.loads(userJSON)
print(user)

print(user['first_name'])

###################################
## Description: Serialize to JSON
###################################
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)
print(carJSON)