import turtle
import time
start_points = (0, -20, -40)
turtles = []
screen = turtle.Screen()
class snake():

    def __init__(self):
        tim = turtle.Turtle()
        screen.setup(height=600, width=600)
        screen.bgcolor("black")
        screen.tracer(0)
        
    def move():     
        for postion in start_points:
            turtle_i = turtle.Turtle()
            turtle_i.pu()
            turtle_i.shape("square")
            turtle_i.color("white")
            turtle_i.goto(postion, 0)
            turtles.append(turtle_i)

        screen.update()
        is_game_on = True
        while is_game_on:
            screen.update()
            time.sleep(0.2)
            for num in range(len(turtles) - 1, 0, -1):
                new_x = turtles[num - 1].xcor()
                new_y = turtles[num - 1].ycor()
                turtles[num].goto(new_x, new_y)
            turtles[0].fd(20)


snake.move()
screen.exitonclick()