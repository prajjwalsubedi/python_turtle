import turtle as t
import random


is_race_on = False
colors = [
    "red", "green", "blue", "purple", "yellow", "brown", "magenta", "maroon"
]
turtles = []
screen = t.Screen()
screen.setup(width=500, height=400)

#input

user_input = screen.textinput(
    title="Make Your Bet.",
    prompt="Which color turtle will win the race? enter a color:  ")

y = 125
x = 0
for color in colors:
    turtle_x = t.Turtle()
    turtle_x.pu()
    turtle_x.shape("turtle")
    turtle_x.color(color)
    turtle_x.speed("fastest")
    turtles.append(turtle_x)
    turtle_x.goto(-250, y)
    y -= 25
    turtle_x.seth(0)
    x += 1
if user_input:
	is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_input:
                print(f"You WON!!! The {winning_color} has won the race.")
            else: 
                print(f"You LOST!!! The {winning_color} has won the race.")
        else:
        	turtle.fd(random.randint(0, 5))
 


screen.exitonclick()
