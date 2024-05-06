from .maps import print_map

def map_command(func):
    def wrapper(*args, **kwargs):
        print(f'Executing {func.__name__}')
        func(*args, **kwargs)
        print_map()
    return wrapper
