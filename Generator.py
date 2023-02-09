import random
import secrets
import string

letters = string.ascii_letters
numbers = string.digits

length = int(input("Password Length: "))

password = "".join([random.choice( letters + numbers) for o in range(length)])

print(password)
