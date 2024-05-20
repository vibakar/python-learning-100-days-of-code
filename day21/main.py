from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# for position in range(310, -310, -50):
#     turtle = Turtle()
#     turtle.shape("square")
#     turtle.speed("fastest")
#     turtle.color("white")
#     turtle.shapesize(0.5, 0.3)
#     turtle.penup()
#     turtle.goto(0, position)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.move_up_paddle, "w")
screen.onkey(left_paddle.move_down_paddle, "s")
screen.onkey(right_paddle.move_up_paddle, "Up")
screen.onkey(right_paddle.move_down_paddle, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()