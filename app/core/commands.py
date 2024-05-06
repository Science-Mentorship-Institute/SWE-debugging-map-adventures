from .decorators import map_command
from .player import player

@map_command
def move_right():
    player.move(1, 0)


@map_command
def move_left():
    player.move(-1, 0)


@map_command
def move_up():
    player.move(0, -1)


@map_command
def move_down():
    player.move(0, 1)
