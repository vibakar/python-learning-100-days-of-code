from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.listen()
screen.setup(width=500, height=400)
colours = ["red", "orange", "yellow", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a user_bet:")
space = 60
all_turtles = []

for colour in colours:
    new_turtle = Turtle()
    new_turtle.shape(name="turtle")
    new_turtle.color(colour)
    new_turtle.penup()
    new_turtle.goto(-230, space)
    all_turtles.append(new_turtle)
    space-= 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You lose! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()