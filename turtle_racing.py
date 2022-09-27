import turtle as t
import random
colors = ["red", "green", "blue", "purple", "yellow", "brown", "magenta", "maroon"]
turtles = {}
screen = t.Screen()
y = 0
x = 0
for color in colors:
    turtle_x = t.Turtle()
    turtle_x.shape("turtle")
    turtle_x.color(color)
    turtle_x.speed("fastest")
    dict = {color : turtle_x}
    turtles.update(dict)
    turtle_x.seth(150)
    turtle_x.forward(400)
    turtle_x.seth(270)
    turtle_x.fd(y)
    y += 50
    turtle_x.seth(0)
    x += 1



print(turtles["red"])

screen.exitonclick()

