# Typles in Python

fruits_list = ['Apples', 4, "Bananas", 5, "Oranges", 6]
print(type(fruits_list))
print(fruits_list)

fruits_tuple = ('Apples', 4, "Bananas", 5, "Oranges", 6)
print(type(fruits_tuple))
print(fruits_tuple)

# we can modify elements within a list
fruits_list[0] = "Strawberries"

# we can NOT modify elements within a tuple
# fruits_tuple[0] = "Strawberries"
# print(fruits_tuple)
# TypeError: 'tuple' object does not support item assignment

# We can perform similar operations on tuples like we can with lists
# Slicing
print(fruits_tuple[2:5])
print(fruits_list[2:5])

# Recalling elements
print(fruits_tuple[0])
print(fruits_list[0])

# Concatenation of tuples
fruits_tuple = fruits_tuple[:4] + ("Cherries", 10)
print(fruits_tuple)

# Tuples with one element
x = (5)     # type = int
print(type(x))

x = (5, )   # type = tuple --> This is the notation for a tuple with 1 element
print(type(x))

# We can find the lenght of a tuple
print(len(fruits_tuple))

# Creating a tuple
another_tuple = tuple(("Hello", 18, True))
print(another_tuple)
print(type(another_tuple))

# Converting a tuple to a list and than back to a tuple!
fruits_tuple = list(fruits_tuple)
fruits_tuple.append("Pears")
fruits_tuple = tuple(fruits_tuple)
print(fruits_tuple)

# Unpacking tuples
fruits_tuple = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
(one, two, three, four, five) = fruits_tuple
print(one) # --> Apples
print(two) # --> Bananas
print(tuple(three)) # --> ('P', 'e', 'a', 'r', 's')

# Incorporate loops within tuples
for i in range(len(fruits_tuple)):
    print(fruits_tuple[i])