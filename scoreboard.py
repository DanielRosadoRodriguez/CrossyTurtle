from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-250, y=250)
        self.write(arg=f"Score: {self.level}", font=('Montserath', 10, 'normal'))
        self.print_score_board()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.print_score_board()

    def print_score_board(self):
        self.write(arg=f"Score: {self.level}", font=('Montserath', 10, 'normal'))

    
