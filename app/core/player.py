class Player:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.character = 'P'

    def move(self, dx, dy):
        self.x += 2 * dx
        self.y += dy
