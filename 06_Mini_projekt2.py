# Turtle project

import turtle

# Környezet beállítása
turtle.bgcolor('black')
turtle.pensize(2)
turtle.color('red')
turtle.speed(0)

# Draw a square
turtle.forward(50) # előre
turtle.left(90)    # fordul
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
# turtle.done() # Nem zárul be az ablak a végén

# Nice little project
# for colours in ['red', 'orange', 'yellow', 'green', 'blue', 'purple']:
#    turtle.color(colours)
#    turtle.circle(150)
#    turtle.left(60)
# turtle.done()

# Let's make it cooler
for i in range(6):
    for colours in ['red', 'orange', 'yellow', 'green', 'blue', 'purple']:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(10)
turtle.done()