#Create a function that generates a random password with a mix of uppercase, lowercase, digits, and special characters.
import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choices(all_characters, k=length))

    return password

print("Generated Password:", generate_password(12))
