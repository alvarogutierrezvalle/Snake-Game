from turtle import Turtle

# First position for a body with 3 part
FIRST_POSITION = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

# Angles to turn
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in FIRST_POSITION:
            new_seg = Turtle(shape='square')
            new_seg.color('white')
            new_seg.penup()
            new_seg.goto(position)
            self.body.append(new_seg)

    def increase(self):
        new_seg = Turtle(shape='square')
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(self.body[-1].position())
        self.body.append(new_seg)

    def wall_collision(self):
        return self.head.xcor() in (300, -300) or self.head.ycor() in (300, -300)

    def tail_collision(self):
        for part in self.body[1:]:
            return self.head.distance(part) < 10

    def reset(self):
        for sef in self.body:
            sef.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def go_forward(self):
        for seg in range(len(self.body) - 1, 0, -1):
            newx = self.body[seg - 1].xcor()
            newy = self.body[seg - 1].ycor()
            self.body[seg].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
