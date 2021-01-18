# Test yourself quiz!

# Question 1 - Assigning Variables
x = 10
y = 3
print(x * y) # Multiplication
print(x + y) # Addition
print(x - y) # Substraction
print(x / y) # Division

# Question 2 - Lists
my_list = list(range(0, 101, 2))
print(my_list)

print(my_list[0:10]) # Printing the first ten elements

print(len(my_list)) # Finding the length of the list

my_list.append(True)    # Appending a value to this list - can be any type
print(my_list)

# Question 3 - If statement
number = 835
if number % 5 == 0:
    print("number is divisible by 5")
else:
    print("number is not devisible by 5")

# Question 4 - For loop
for i in range(6):
    print(i)

# Question 5 - Turtle
import turtle

for i in range(5): # A pentagon has five sides
    turtle.right(72) # 360 / 5 = 72
    turtle.forward(180)
turtle.done()

# Question 6 - Functions
def pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

print(pythagorean_triple(3, 4, 5)) # This is True
print(pythagorean_triple(3, 9, 15)) # This is False

# Question 7 - Spot the Error!
# n = 5
# while n > 0
# n = n + 1
#     print(n)

n = 5
while n < 20:
    n = n + 1
    print(n)

# Question 8 - Plotting!
import matplotlib.pyplot as plt

list1 = [1, 6, 13, 16, 24]
list2 = [3, 7, 17, 28, 30]

plt.plot(list1, list2, c = "blue", linewidth=1, label="A Line!", linestyle="dashed",
         marker="s", markerfacecolor="purple", markersize=2)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Python Plot of a Line")
plt.legend()
plt.show()