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


def ship_placement(start_position, end_position):

    # Same letters, different numbers
    if(start_position[0] == end_position[0]):

        start_number = int(start_position[1])
        end_number = int(end_position[1])

        if(start_number > end_number):

            start_number, end_number = reverse_variables(start_number, end_number)

        for position_number in range(start_number, end_number + 1):
            cell = start_position[0] + str(position_number)
            for (grid_x, grid_y), element in np.ndenumerate(grid):
                if element == cell:
                    grid[grid_x, grid_y] = "##"


    # Same numbers, different letters
    elif(start_position[1]) == end_position[1]:

        start_letter = ord(start_position[0])
        end_letter = ord(end_position[0])

        if(start_letter > end_letter):
            
            start_letter, end_letter = reverse_variables(start_letter, end_letter)

        for position_letter in range(start_letter, end_letter + 1):
            cell = chr(position_letter) + start_position[1]
            for (grid_x, grid_y), element in np.ndenumerate(grid):
                if element == cell:
                    grid[grid_x, grid_y] = "##"

    else:
        print("invalid placement")

    return