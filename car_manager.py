import random
from turtle import Turtle
from random import choice

COLORS = ["red", "yellow", "blue", "green", "purple", "black"]
MOV_DISTANCE = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.max_chance = 6

    def create_car(self):

        car_chance = random.randint(1, self.max_chance)
        if car_chance == 1:
            color = choice(COLORS)
            random_ycor = random.randint(-220, 220)
            car = Turtle(shape="square")
            car.penup()
            car.color(color)
            car.setheading(180)
            car.goto(x=320, y=random_ycor)
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(MOV_DISTANCE)

    def reduce_max_chance(self):
        if self.max_chance > 1:
            self.max_chance -= 1
