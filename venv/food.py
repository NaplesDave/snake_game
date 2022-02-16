from turtle import Turtle
import random


class Food(Turtle):  # Inherit from Turtle class

    def __init__(self):  # Initialize the class
        super().__init__()  # Initialize the Super - Turtle Parent class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

