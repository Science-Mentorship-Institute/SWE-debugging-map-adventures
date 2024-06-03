from core.commands import *
from core.player import Player
from core.game import Game
from core.decorators import init_map
from core.maps import read_map
import os
import time


def initialize() -> Game:
    os.system('clear')
    player = Player(0, 0)
    map = read_map('maps/exercise1.txt')
    init_map(map)
    game = Game(player, map, num_destinations=3)
    print("Original layout")
    game.print_map()
    return game

''' In exercise 1 students will explore move commands '''

def main():
    game = initialize()

    # type commands here
    change_player_color(game, "blue")
    move_right(game)
    move_right(game)
    move_right(game)
    move_right(game)
    move_down(game)
    move_left(game)
    move_down(game)
    move_down(game)
    move_down(game)
    move_left(game)
    move_left(game)
    move_up(game)
    move_up(game)
    move_up(game)
    move_right(game)
