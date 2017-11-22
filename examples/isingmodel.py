import sys
sys.path.append('..')

import matplotlib.pyplot as plt
from matplotlib import animation

import numpy as np
from Gimli.World import World

def func(own,up,down,left,right,upright,downright,upleft,downleft):
    #sum = up + down + left + right + upright + downright + upleft + downleft
    energy = up + down + left + right
    spin = 1
    if energy < 0:
        spin = -1
    if energy == 0:
        spin = np.random.choice([1,-1])
    return spin

size = [100,100]
initialcells = np.random.choice([1,-1],size=size)
world = World(func,size=size,initialcells=initialcells)
cells = world.getcells()

fig = plt.figure()
im = plt.imshow(cells,interpolation='none',cmap='gray')


def animate(i):
    world.update()
    cells = world.getcells()
    im.set_array(cells)
    return [im]

anim = animation.FuncAnimation(fig,animate,frames=200, interval=60, blit=True)
plt.show()