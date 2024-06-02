class Player:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.character = 'P'

    def move(self, dx, dy):
        self.x += 2 * dx
        self.y += dy
    
    def change_color(self, color):
        if color == "red":
            self.character = "\033[91mP\033[00m"
        elif color == "green":
            self.character = "\033[92mP\033[00m"
        elif color == "purple":
            self.character = "\033[95mP\033[00m"
        elif color == "blue":
            self.character = "\033[96mP\033[00m"
        else:
            self.character = "P"
