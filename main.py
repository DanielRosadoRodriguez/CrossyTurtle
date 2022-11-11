import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()

car_manager = CarManager()

scoreboard = Scoreboard()
screen.onkey(key="w", fun=player.move_forward)

cont = 0
game_is_on = True
while game_is_on:
    cont += 1
    time.sleep(0.1)
    screen.update()
    car_manager.move_car()
    if cont % 10 == 0:
        car_manager.create_car()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            print("game over")
            game_is_on = False
            break
    if player.ycor() > 250:
        scoreboard.update_scoreboard()
        player.reset_positon()
screen.exitonclick()