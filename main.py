from turtle import Screen, Turtle
import time
from snake import Snake
snake = Snake()
screen = Screen()
screen.title("My Snake Game")
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()








screen.exitonclick()