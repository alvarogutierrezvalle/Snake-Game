from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("highscore.txt", 'r') as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("highscore.txt", 'w') as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def refresh(self):
        self.clear()
        self.score += 1
        self.update()
