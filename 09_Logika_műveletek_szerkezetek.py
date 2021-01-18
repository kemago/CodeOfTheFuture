# Booleans

print(True)
print('True')

print(type(True))
print(type('True'))

print(5 == 5)
print(6 == 5)

# If statement
x = 10
y = 6
if x % y == 0: # % modulus
    print(True)
else:
    print(False)

# While loop
number = 1
while number < 4:
    print(number)
    if number == 2:
        break
    number = number + 1

number = 2
while number < 4:
    print(number)
    number = number + 1
else:
    print('number is no longer less than 4') # a szám már nagyobb vagy egyenlő, mint négy

# if statement with elif
number = 1
if number > 0:
    print('Positive Number')
elif number == 0:
    print('Zeto')
else:
    print('Negative Number')