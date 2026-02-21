from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
l_score = Scoreboard((-100, 250))
r_score = Scoreboard((100, 250))

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

default_sleep = 0.1
game_on = True

while game_on:
    try:
        time.sleep(default_sleep)
        screen.update()
        
        ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)

        if ball.ycor() >= 290 or ball.ycor() <= -290:
            ball.y_move *= -1

        if (ball.xcor() >= 330 and ball.distance(r_paddle) <= 50) or (ball.xcor() <= -330 and ball.distance(l_paddle) <= 50):
            ball.x_move *= -1
            if default_sleep > 0.01:
                default_sleep *= 0.9

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.x_move *= -1
            default_sleep = 0.1
            l_score.increase_score()

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.x_move *= -1
            default_sleep = 0.1
            r_score.increase_score()

    except:
        game_on = False