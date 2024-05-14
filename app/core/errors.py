class ObstacleError(Exception):
    def __init__(self):
        self.message = 'Your player has run into an obstacle'
        super().__init__(self.message)