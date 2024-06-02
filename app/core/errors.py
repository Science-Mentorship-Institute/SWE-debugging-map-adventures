class ObstacleError(Exception):
    def __init__(self):
        self.message = '\033[91mYour player has run into an obstacle \033[00m'
        super().__init__(self.message)