from .game import Game
from .errors import IllegalArgumentException
import time
import os

def init_map(map):
    global current_map, command_num
    current_map = map
    command_num = 1


def map_command(func):
    def wrapper(*args, **kwargs):
        if (len(args) != 1):
            raise IllegalArgumentException()
        global command_num
        os.system('clear')
        print(f'Instruction {command_num}: {func.__name__}')
        func(*args, **kwargs)
        command_num += 1
        if type(args[0]) == Game:
            args[0].print_map()
        time.sleep(1)

    return wrapper

def color_command(func):
    def wrapper(*args, **kwargs):
        if (len(args) != 2):
            raise IllegalArgumentException()
        os.system('clear')
        global command_num
        os.system('clear')
        print(f'Instruction {command_num}: {func.__name__}')
        func(*args, **kwargs)
        command_num += 1
        if type(args[0]) == Game:
            args[0].print_map()
        time.sleep(1)

    return wrapper
