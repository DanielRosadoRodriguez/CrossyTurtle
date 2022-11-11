from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.color('black')
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-280)

    def move_forward(self):
        self.goto(x=self.xcor(), y=self.ycor()+20)

    def reset_positon(self):
        self.goto(x=0, y=-280)

