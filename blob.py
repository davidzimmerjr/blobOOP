import random

class Blob:
    
    def __init__(self, color, x_boundary, y_boundary, size_range, movement_range, overbound=0):
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(x_boundary)
        self.y = random.randrange(y_boundary)
        self.size = random.randint(size_range[0], size_range[1])
        self.color = color
        self.movement_range = movement_range
        self.overbound = overbound

    def move(self):
        self.move_x = random.randrange(self.movement_range[0],self.movement_range[1])
        self.move_y = random.randrange(self.movement_range[2],self.movement_range[3])
        self.x += self.move_x
        self.y += self.move_y

    def checkbounds(self):
        if self.x < 0: self.x = 0
        elif self.x > self.x_boundary + self.overbound: self.x = self.x_boundary + self.overbound

        if self.y < 0: self.y = 0
        elif self.y > self.y_boundary + self.overbound: self.y = self.y_boundary + self.overbound
