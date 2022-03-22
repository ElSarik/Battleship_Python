import numpy as np
import string

from calculations import reverse_variables

def grid_init():
    global grid

    size = 10

    letters = list(string.ascii_uppercase)
    list_grid = []
    

    for row in range(size):
        list_grid.append([letters[row] + str(column) for column in range(size)])

    grid = np.array(list_grid)


def grid_display():
    print(grid)


