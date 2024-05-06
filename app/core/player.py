class Player:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Global Player object
player = Player(0, 0)
