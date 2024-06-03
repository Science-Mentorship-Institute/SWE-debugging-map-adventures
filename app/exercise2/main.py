from core.commands import *
from core.player import Player
from core.game import Game
from core.decorators import init_map
from core.maps import read_map
import os


def initialize() -> Game:
    os.system('clear')
    player = Player(0, 0)
    map = read_map('maps/exercise2.txt')
    init_map(map)
    game = Game(player, map, num_destinations=3)
    print("Original layout")
    game.print_map()
    return game

''' In exercise 2 students will explore iterative commands '''

def main():
    game = initialize()

    # type commands here
    change_player_color(game, "blue")
    move_right(game)
    move_down_n_times(game, n=3)
    move_right(game)
    move_down(game)
    move_left_n_times(game, n=1)
    move_down_n_times(game, n=2)
