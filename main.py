from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


snake = Snake()
screen = Screen()
screen.title("My Snake Game")
screen.setup(height=500, width=600)
screen.bgcolor("black")
screen.tracer(0)

food = Food()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)

    # Detect collision with food.

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 260 or snake.head.xcor() < -260 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
        is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for seg in snake.cobra[1:]:
        if snake.head.distance(seg) < 10:
            is_on = False
            scoreboard.game_over()


    snake.move()








screen.exitonclick()