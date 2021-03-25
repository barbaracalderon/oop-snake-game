from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
initial_coordinate = [(0, 0), (-20, 0), (-40, 0)]
snake = []

for position in initial_coordinate:
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(position)
    snake.append(new_turtle)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    for seg_num in range(len(snake)-1, 0, -1):           # range(start=len(segments)-1, end=0, step=-1)
        new_x = snake[seg_num-1].xcor()
        new_y = snake[seg_num].ycor()
        snake[seg_num].goto(new_x, new_y)
    snake[0].forward(20)










screen.exitonclick()