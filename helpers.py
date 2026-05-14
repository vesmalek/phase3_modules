#     - calculate_discount(price, percent) → returns discounted price

def calculate_discount(price, percent):
    return price * (1 - (percent/100))

#     - greet_user(username) → returns "Welcome, {username}!"

def greet_user(username):
    return f'Welcome, {username}!'

#     - is_valid_password(password) → returns True if len >= 8, False otherwise

def is_valid_password(password):
    if len(password) >= 8:
        return True
    else:
        return False