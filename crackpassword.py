import string
from random import *

u_pwd = input("Enter password: ")
pwd = string.ascii_letters + string.digits + string.punctuation 
#or
#pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6']

pw = ""
attempts = 0

while pw != u_pwd:
    pw = ""
    for _ in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, len(pwd)-1)]
        pw += str(guess_pwd)
    attempts += 1
    print(f"Attempt {attempts}: {pw}")
    print("Cracking Password....Please wait")

    if pw == u_pwd:
        break
print("Your password is:", pw)
print("Password cracked in", attempts, "attempts.")
