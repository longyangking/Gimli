# Author: Yang Long <longyang_123@yeah.net>
#
# License: LGPL-2.1

import numpy as np

class Rule:
    def __init__(self,rulefunc):
        self.rulefunc = rulefunc

    def evaluate(self,sizeX,sizeY,neigbors):
        (own,up,down,left,right,upright,downright,upleft,downleft) = neigbors

        cells = np.zeros([sizeX,sizeY])
        for i in range(sizeX):
            for j in range(sizeY):
                cells[i][j] = self.rulefunc(own[i][j],up[i][j],down[i][j],\
                            left[i][j],right[i][j],upright[i][j],\
                            downright[i][j],upleft[i][j],downleft[i][j])

        return cells