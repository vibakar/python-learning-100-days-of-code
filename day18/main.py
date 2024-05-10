from turtle import Turtle, Screen
import random

turtle = Turtle()
# turtle.shape("arrow")
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# screen = Screen()
# screen.exitonclick()
#####################################################################

# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# screen = Screen()
# screen.exitonclick()
#####################################################################

# for sides in range(3, 11):
#     for _ in range(sides):
#         angle = int(360/sides)
#         turtle.forward(100)
#         turtle.right(angle)

# screen = Screen()
# screen.exitonclick()
#####################################################################

# direction = [0, 90, 180, 270]
# directions = [0, 90, 180, 270]
# turtle.pensize(15)
# turtle.speed("fastest")

# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# screen = Screen()
# screen.colormode(255)

# for _ in range(200):
#     turtle.pencolor(random_colour())
#     turtle.forward(30)
#     turtle.setheading(random.choice(direction))

# screen.exitonclick()
#####################################################################
# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# turtle.speed("fastest")
# screen = Screen()
# screen.colormode(255)

# for n in range(int(360/10)):
#     turtle.pencolor(random_colour())
#     turtle.circle(100)
#     curent_heading = turtle.heading()
#     turtle.setheading(curent_heading + 10)

# screen.exitonclick()
#####################################################################
import colorgram
rgb_colors = []
colors = colorgram.extract('image.webp', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

screen = Screen()
screen.colormode(255)

turtle.speed("fastest")
turtle.hideturtle()
turtle.setheading(255)
turtle.penup()
turtle.forward(300)
turtle.setheading(0)

number_of_dots = 100

for dots in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(rgb_colors))
    turtle.forward(50)

    if dots % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen.exitonclick()