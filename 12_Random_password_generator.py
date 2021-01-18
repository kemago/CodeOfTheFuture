import random
from random import randint

# All uppercase password
password = ''
for i in range(10):
    i = chr(randint(65, 90))  # uppercase letters
    password = str(password) + i
print(password)

# Upper and lowercase password
password = ''
for i in range(5):
    i = chr(randint(65, 90))  # uppercase letters
    for j in range(5):
        j = chr(randint(65, 90)).lower()
    password = str(password) + i + j
print(password)