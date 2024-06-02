from .decorators import map_command
from .game import Game

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
