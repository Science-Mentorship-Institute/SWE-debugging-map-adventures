class ObstacleError(Exception):
    def __init__(self):
        self.message = '\033[91mYour player has run into an obstacle \033[00m'
        super().__init__(self.message)

class IllegalArgumentException(Exception):
    def __init__(self):
        self.message = '\033[91mYour function call has illigal number of parameters \033[00m'
        super().__init__(self.message)