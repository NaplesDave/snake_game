from turtle import Screen, Turtle
import time

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()  # Create a new Snake object

screen.listen()  # Listen for keystrokes
screen.onkey(snake.up, "Up")  # Up arrow pressed
screen.onkey(snake.down, "Down")  # Down arrow is pressed
screen.onkey(snake.left, "Left")  # Left arrow is pressed
screen.onkey(snake.right, "Right")  # Right arrow is pressed

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
