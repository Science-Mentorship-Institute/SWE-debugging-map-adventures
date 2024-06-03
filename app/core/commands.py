from .decorators import map_command
from .game import Game
import os

@map_command
def pause(g: Game):
    g.print_map()
    input("Press Enter to continue...")
    os.system('clear')

@map_command
def move_right(g: Game, n=1):
    g.move(1, 0)


@map_command
def move_left(g: Game, n=1):
    g.move(-1, 0)

@map_command
def move_up(g: Game, n=1):
    g.move(0, -1)


@map_command
def move_down(g: Game, n=1):
    g.move(0, 1)


def move_right_n_times(g: Game, n):
    for _ in range(n):
        move_right(g)


def move_left_n_times(g: Game, n):
    for _ in range(n):
        move_left(g)


def move_up_n_times(g: Game, n):
    for _ in range(n):
        move_up(g)


def move_down_n_times(g: Game, n):
    for _ in range(n):
        move_down(g)


@map_command
def change_player_color(g: Game, color):
    g.change_player_color(color)
