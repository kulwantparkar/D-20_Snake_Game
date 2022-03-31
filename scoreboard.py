from turtle import Turtle
turtle = Turtle()

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)



    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()


