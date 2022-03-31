from turtle import Turtle, Screen
screen = Screen()
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.cobra = []
        self.create_snake()
        self.head = self.cobra[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        kai = Turtle()
        kai.color("white")
        kai.shape("square")
        kai.penup()
        kai.goto(position)
        self.cobra.append(kai)

    def extend(self):
        self.add_segment(self.cobra[-1].position())

    def move(self):
        for coco in range(len(self.cobra)-1, 0, -1):
            x_position = self.cobra[coco-1].xcor()
            y_position = self.cobra[coco - 1].ycor()
            self.cobra[coco].goto(x_position, y_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(LEFT)

