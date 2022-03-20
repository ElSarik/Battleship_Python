import numpy as np
import string

def grid_init():
    global grid

    size = 10

    letters = list(string.ascii_uppercase)
    grid = []

    for row in range(size):
        grid.append([letters[row] + str(column) for column in range(size)])


def grid_display():
    print(np.matrix(grid))


