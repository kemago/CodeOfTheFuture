# Functions in Python

# Function that returns x^2
def squared(x):
    result = x**2
    return result

print(squared(10))

# Function that returns x^2 + y**2
def squared(x, y):
    result = x**2 + y**2
    return result

print(squared(10, 2))

# A new function
def born(country):
    return print('I am from ' + country)

born('England')