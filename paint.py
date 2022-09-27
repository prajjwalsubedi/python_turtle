import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def move_fd():
    tim.fd(10)


def move_bk():
    tim.bk(10)


def rotate_rt():
    tim.setheading(tim.heading() + 5)


def rotate_lt():
    tim.setheading(tim.heading() - 5)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_fd, "w")
screen.onkey(move_bk, "s")
screen.onkey(rotate_lt, "a")
screen.onkey(rotate_rt, "d")
screen.onkey(clear, "space")
screen.exitonclick()
