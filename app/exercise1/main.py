from core.commands import *

'''
In exercise 1 students will explore:
    * move commands
    * change color command
    * exceptions
'''

def play(game):
    change_player_color(game, "red")
    move_right(game)
    move_right(game)
    #change_player_color(game)  # IlligalArgument Exception 
    move_down(game)
    move_down(game)
    move_down(game)  # Obstacle Exception