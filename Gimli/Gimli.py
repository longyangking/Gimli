# Author: Yang Long <longyang_123@yeah.net>
#
# License: LGPL-2.1

import numpy as np

class Gimli:
    def __init__(self,func,size,boundary=None,\
            initialcells=None,verbose=False):
        self.func = func
        self.size = size
        self.boundary = boundary
        if initialcells is not None:
            self.cells = initialcells
        else:
            self.cells = 1*(np.random.random(size)<0.5)

    def update(self):
        
        if self.verbose:
            ## TODO
