import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("red")
        self.refresh()



    def refresh(self):
        rand_x = random.randint(-200, 200)
        rand_y = random.randint(-200, 200)
        self.goto(rand_x, rand_y)