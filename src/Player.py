

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
        
        self.grid[x][y] = 'S'
    
    def create_grid(self, value):

        for i in range(value):
            self.grid.append(['E'] * value)

    def __pre_check(self, x, y):
        x = x-1
        y = y-1
        if x < 0 or y < 0:
            return true
        if x >= self.size or y >= self.size:
            return true
        return false


