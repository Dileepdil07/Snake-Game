import random
from turtle import Turtle


class Food (Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def super_food(self):
        self.shapesize(stretch_wid=0.9, stretch_len=0.9)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
