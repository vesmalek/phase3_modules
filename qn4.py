# Q4. Generate a random token using random and string modules
#     Write a function called generate_token(length=10) that returns
#     a random mix of letters and digits of the given length
#     Call it twice — once with default length, once with length=20

import random
import string

def generate_token(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

print()
print(generate_token())
print(generate_token(20))