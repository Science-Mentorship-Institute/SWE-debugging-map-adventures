from .game import Game
import time
import os

def init_map(map):
    global current_map, command_num
    current_map = map
    command_num = 1


def map_command(func):
    def wrapper(*args, **kwargs):
        global command_num
        os.system('clear')
        print(f'Instruction {command_num}: {func.__name__}')
        func(*args, **kwargs)
        if type(args[0]) == Game:
            args[0].print_map()
        command_num += 1
        time.sleep(.5)

    return wrapper
