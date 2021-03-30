from turtle import Turtle

class Snake:

    def __init__(self):
        self.initial_coordinate = [(0, 0), (-20, 0), (-40, 0)]
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in self.initial_coordinate:
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.snake.append(new_turtle)

    def move(self):
        global seg_num
        for seg_num in range(len(self.snake) - 1, 0, -1):  # range(start=len(segments)-1, end=0, step=-1)
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(20)
