from turtle import Screen
import time
# David King Feb 16, 2022 ... PYTHON 100 Days of Code Class Challenge / UDEMY
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()  # Create a new Snake object
food = Food()
scoreBoard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:  # Less than 15 pixels from head to food...do this
        food.refresh()
        scoreBoard.score += 1
        scoreBoard.scoreboard_update()
        snake.extend()

# Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreBoard.game_over()

    # Detect collision with its own tail
    for segment in snake.segments:
        if segment == snake.head:  # Skip the head of the snake itself
            pass
        elif snake.head.distance(segment) < 10:  # Check the est of the snake segment positions for distance less
            # Then 10 pixels
            game_is_on = False
            scoreBoard.game_over()


screen.exitonclick()
