import numpy as np
import string

from calculations import reverse_variables

available_ships = [2, 3, 3, 4, 5]

ship_tile = "██"
fire_miss_tile = "▒▒"
ship_hit_tile = "╬╬"


def grid_init():
    global grid
    global letters

    size = 10

    letters = list(string.ascii_uppercase)
    list_grid = []
    

    for row in range(size):
        list_grid.append([letters[row] + str(column) for column in range(size)])

    grid = np.array(list_grid)


def grid_display():
    print(grid)


def ship_placement(start_position, end_position):

    if ((start_position not in grid) or (end_position not in grid)):
        print("Invalid placement (start, end position)")

    else:

        # Same letters, different numbers
        if(start_position[0] == end_position[0]):

            start_number = int(start_position[1:])
            end_number = int(end_position[1:])

            if(start_number > end_number):

                start_number, end_number = reverse_variables(start_number, end_number)

            if ((end_number - start_number) + 1) not in available_ships:
                print("Invalid ship length!")
                

            else:
                # Replace cells with ship tile.
                for position_number in range(start_number, end_number + 1):
                    cell_code = start_position[0] + str(position_number)
                    for (grid_x, grid_y), element in np.ndenumerate(grid):
                        if element == cell_code:
                            grid[grid_x, grid_y] = ship_tile

                available_ships.remove((end_number - start_number) + 1)


        # Same numbers, different letters
        elif(start_position[1:]) == end_position[1:]:

            start_letter = ord(start_position[0])
            end_letter = ord(end_position[0])

            if(start_letter > end_letter):
                
                start_letter, end_letter = reverse_variables(start_letter, end_letter)

            if ((end_letter - start_letter) + 1) not in available_ships:
                print("Invalid ship length!")
                

            else:
                for position_letter in range(start_letter, end_letter + 1):
                    cell_code = chr(position_letter) + start_position[1:]
                    for (grid_x, grid_y), element in np.ndenumerate(grid):
                        if element == cell_code:
                            grid[grid_x, grid_y] = ship_tile

                available_ships.remove((end_letter - start_letter) + 1)

        else:
            print("Invalid placement (diagonal placement)")

    return


def grid_fire(fired_cell):

    cell_x = int(letters.index(fired_cell[0]))
    cell_y = int(fired_cell[1:])

    if (cell_x > np.size(grid, 0)) or (cell_y > np.size(grid, 1)):
        print("Your shot was out of the board!")

    else:
        for (grid_x, grid_y), element in np.ndenumerate(grid):

            if (cell_x == grid_x) and (cell_y == grid_y):
                
                if element == fired_cell:
                    grid[grid_x, grid_y] = fire_miss_tile
                    print("You missed!")

                elif element == ship_tile:
                    grid[grid_x, grid_y] = ship_hit_tile
                    print("Ship Hit!")

                else:
                    print("Invalid cell! (You have already hit this cell)")

    return