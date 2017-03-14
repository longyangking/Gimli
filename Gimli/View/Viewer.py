# Author: Yang Long <longyang_123@yeah.net>
#
# License: LGPL-2.1

import numpy as np
import matplotlib.pyplot as plt

class Viewer:
    def __init__(self,cells,boundary,):
        self.cells = cells
        self.boundary = boundary
    
    def plot(self):
        fig = plt.figure()
        im = plt.imshow(self.cells,interpolation='none')
        plt.show()

    def anime(self):
        fig = plt.figure()
        im = plt.imshow(self.cells,interpolation='none')
        plt.show()
    
    