class ObstacleError(Exception):
    def __init__(self):
        self.message = '\033[91mYour player has run into an obstacle \033[00m'
        super().__init__(self.message)
    

class OutOfOrderError(Exception):
    def __init__(self):
        self.message = '\033[91mYou have reached the destinations out of order \033[00m'
        super().__init__(self.message)


class OutOfBoundsError(Exception):
    def __init__(self):
        self.message = '\033[91mYour player has moved out of bounds \033[00m'
        super().__init__(self.message)