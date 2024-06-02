from .errors import ObstacleError

class Game:
    def __init__(self, player, map):
        self.player = player
        self.map = map
    

    def move(self, dx, dy):
        self.player.move(dx, dy)
        if self.map[self.player.y][self.player.x] == 'X':
            raise ObstacleError()


    def print_map(self):
        m = [list(row) for row in self.map]
        m[self.player.y][self.player.x] = self.player.character
        for row in m:
            print(''.join(row))
    
    def change_player_color(self, color):
        self.player.change_color(color)
