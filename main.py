from turtle import Screen, Turtle
import time
from Snake import Snake
from Food import Food
from scoreboard import Scoreboard

# ------------SET UP SCREEN--------------------------

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# -----------CREATING OBJECTS---------------------------

score = 1
scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.listen()

screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")

# -----------MAIN LOOP---------------------------

is_game = True

while is_game:
    screen.update()
    time.sleep(0.1)
    snake.go_forward()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.increase()
        scoreboard.refresh()

    if snake.wall_collision():
        scoreboard.reset()
        snake.reset()

    for part in snake.body[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
