import random
from turtle import Turtle

colors = ["red", "blue", 'green', 'peru', 'purple', 'pink', 'chocolate', 'grey', 'cyan', 'brown']


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(colors))
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
