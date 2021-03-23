from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
initial_coordinate = [(0, 0), (-20, 0), (-40, 0)]
snake = []

for position in initial_coordinate:
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.goto(position)
    snake.append(new_turtle)










screen.exitonclick()