

class Player(object):

    def __init__(self):
        self.grid = []
        self.size = None
        self.ships = None
        self.missiles = None

    def add_ship(self, x, y):
        
        if self.__pre_check(x, y):
            print "Wrong inputs provided"
            return
        
        self.grid[x][y] = 1

