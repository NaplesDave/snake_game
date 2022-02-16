from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(-0, 270)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.scoreboard_update()


    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def scoreboard_update(self):
        self.clear()
        self.write(f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

