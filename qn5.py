# Q5. Using the json module:

import json

#     Create a user dict with at least 4 keys

user = {'name': 'John', 'Company': 'ABC Ceramics', 'Address': "5th Str. NY", 'Country': 'Oman'}

#     Convert it to a JSON string and print it
print()
json_string = json.dumps(user)
print(json_string)
print(f"Type: {type(json_string).__name__}")

#     Convert it back to a dict and access one key from the result

print()
user_profile = json.loads(json_string)
print(user_profile)
print(f"Type: {type(user_profile).__name__}")
print()