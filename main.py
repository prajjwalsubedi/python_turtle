# import colorgram
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
import turtle
import random
tim = turtle.Turtle()
tim.ht()
screen = turtle.Screen()
tim.pensize(20)
tim.speed(9)
turtle.colormode(255)

color_list = [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.up()
tim.seth(225)
tim.fd(300)
tim.seth(0)
for y in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.fd(50)
    if y < 9:
        tim.bk(500)
        tim.seth(90)
        tim.fd(50)
        tim.seth(0)






screen.exitonclick()