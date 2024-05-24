from core.commands import move_right, move_down
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
    game = Game(player, map)
    game.print_map()
    return game


def main():
    game = initialize()
    move_right(game)
    move_right(game)
    move_down(game)
    move_down(game)
    move_down(game)