"""
import time
import random
def generate_password(length="12"):
    seed = int(time.time())
    characters = "abcdefghijklmnopqrstuvwxyz1234567890!£$%^&*()_+~#><,./?"
    random.seed(seed)

    password =''.join(random.choice(characters)for _ in range(length))
    return password

password_length = int(input("Enter the desired length for the password: "))

generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")
"""
import secrets
import string

def generate_password(length=""):
    keys = string.ascii_letters + string.digits + string.punctuation
#   keys = "abcdefghijklmnopqrstuvwxyz1234567890!$%^&*()_+-':;?/.,<>#{}[]¬`@"
    password = ''.join(secrets.choice(keys) for _ in range(length))
    return password

password_length = int(input("Enter expected password length: "))

generated_password = generate_password(password_length)
print(f'The generated password is:{generated_password}')