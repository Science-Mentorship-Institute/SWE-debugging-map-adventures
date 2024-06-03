from .decorators import map_command
from .game import Game
import os

@map_command
def pause(g: Game):
    g.print_map()
    input("Press Enter to continue...")
    os.system('clear')

@map_command
def move_right(g: Game):
    g.move(1, 0)


@map_command
def move_left(g: Game):
    g.move(-1, 0)

@map_command
def move_up(g: Game):
    g.move(0, -1)


@map_command
def move_down(g: Game):
    g.move(0, 1)

@map_command
def change_player_color(g: Game, color):
    g.change_player_color(color)
