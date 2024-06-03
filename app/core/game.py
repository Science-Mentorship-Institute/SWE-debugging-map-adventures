from .errors import ObstacleError, OutOfBoundsError, OutOfOrderError

class Game:
    def __init__(self, player, map, num_destinations):
        self.player = player
        self.map = map
        self.num_destinations = num_destinations
        self.curr_destination = 'A'
    

    def move(self, dx, dy):
        self.player.move(dx, dy)
        if self.map[self.player.y][self.player.x] == 'X':
            raise ObstacleError()
        if self.player.x < 0 or self.player.x >= len(self.map[0]) or self.player.y < 0 or self.player.y >= len(self.map):
            raise OutOfBoundsError()
        if self.map[self.player.y][self.player.x] >= 'A' and self.map[self.player.y][self.player.x] < chr(ord('A') + self.num_destinations) and self.map[self.player.y][self.player.x] > self.curr_destination:
            raise OutOfOrderError()
        if self.map[self.player.y][self.player.x] == self.curr_destination:
            self.curr_destination = chr(ord(self.curr_destination) + 1)
            if self.curr_destination == chr(ord('A') + self.num_destinations):
                # Print the map with the player at the final destination with a win statement in green
                print('\033[92mCongratulations! You have reached all destinations in order!\033[00m')



    def print_map(self):
        m = [list(row) for row in self.map]
        m[self.player.y][self.player.x] = self.player.character
        for row in m:
            print(''.join(row))
    
    def change_player_color(self, color):
        self.player.change_color(color)
