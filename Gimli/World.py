import numpy as np
import Rule

class World:
    def __init__(self,rulefunc,size,initialcells=None,\
                verbose=False):

        self.rule = Rule.Rule(rulefunc)
        self.size = size
        self.initialcells = initialcells
        self.verbose = verbose

        if initialcells is not None:
            self.cells = initialcells
        else:
            self.cells = 1.0*(np.random.random(size)<0.5)

        # TODO define boundary
        self.x = np.array(range(1,size[0]-1))
        self.y = np.array(range(1,size[1]-1))
        self.cells[0,:] = 0
        self.cells[:,0] = 0
        self.cells[-1,:] = 0
        self.cells[:,-1] = 0

    def update(self):
        
        own = self.cells[1:-1,1:-1]
        up = self.cells[1:-1,2:]
        down = self.cells[1:-1,:-2]
        left = self.cells[:-2,1:-1]
        right = self.cells[2:,1:-1]
        upright = self.cells[2:,2:]
        downright = self.cells[2:,:-2]
        upleft = self.cells[:-2,2:]
        downleft = self.cells[:-2,:-2]
        neigbors = (own,up,down,left,right,upright,downright,upleft,downleft)

        sizeX = np.size(self.x)
        sizeY = np.size(self.y)
        self.cells[1:-1,1:-1] = self.rule.evaluate(sizeX,sizeY,neigbors)

    def getcells(self):
        return self.cells