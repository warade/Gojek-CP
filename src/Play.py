from Player import Player

class Play(object):

    def __init__(self):
        self.players = {}
        for i in range(1, 3):
            self.players[i] = Player()

    def set_grid(self, value):
        
        for i in range(1, 3):
            self.players[i].create_grid(value)

    def set_battleship(self, value):

        for i in range(1, 3):
            self.players[i].ships = value

    def add_ships(self, idx, x, y):

        # check for valid idx

        self.players[idx].add_ship(x, y)

    def set_missiles(self, value):
        
        # check for valid value

        for i in range(1, 3):
            self.players[i].missiles = value

    def target_opponent(self, idx, x, y):

        # check for validity
        
        if self.players[idx].grid[x][y] == 'S':
            self.players[idx].grid[x][y] = 'D'
        else self.players[idx].grid[x][y] = 'M'






