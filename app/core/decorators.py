from .game import Game

def init_map(map):
    global current_map, command_num
    current_map = map
    command_num = 0


def map_command(func):
    def wrapper(*args, **kwargs):
        global command_num
        print(f'Instruction {command_num}: {func.__name__}')
        func(*args, **kwargs)
        command_num += 1
        if type(args[0]) == Game:
            args[0].print_map()
    return wrapper
