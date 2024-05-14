from core.commands import move_right, move_down
from core.player import Player
from core.game import Game
from core.decorators import init_map
from core.maps import read_map


def initialize() -> Game:
    player = Player(0, 0)
    map = read_map('maps/exercise1.txt')
    init_map(map)
    return Game(player, map)


def main():
    game = initialize()
    game.print_map()
    move_right(game)
    move_down(game)