from turtle import Turtle
FONT = ("Arial", 10, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.print_score_board()
        self.penup()
        self.goto(x=-250, y=250)
        self.print_score_board()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.print_score_board()

    def print_score_board(self):
        self.write(arg=f"Score: {self.level}", font=FONT)

    def print_game_over(self):
        self.write(arg="Game Over", font=FONT)
