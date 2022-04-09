import os
import numpy as np
import string

from messages import *

from calculations import reverse_variables


ship_tile = "██"
fire_miss_tile = "▒▒"
ship_hit_tile = "╬╬"



def grid_init():
    global letters

    size = 10

    letters = list(string.ascii_uppercase)
    list_grid = []
    

    for row in range(size):
        list_grid.append([letters[row] + str(column) for column in range(size)])

    grid = np.array(list_grid)

    return(grid)


def grid_display(grid):
    print(grid)


def ship_placement(grid, available_ships, player):

    while available_ships != []:
        
        grid_display(grid)
        print("")
        print(f"{player} place your ships!")
        print(f"{remaining_ship_sizes()}{available_ships}")
        start_position, end_position = input(enter_ship_coordinates()).split()

        if ((start_position not in grid) or (end_position not in grid)):
            print(ship_placement_invalid())

        else:

            # Same letters, different numbers
            if(start_position[0] == end_position[0]):

                start_number = int(start_position[1:])
                end_number = int(end_position[1:])

                if(start_number > end_number):

                    start_number, end_number = reverse_variables(start_number, end_number)

                if ((end_number - start_number) + 1) not in available_ships:
                    print(ship_length_invalid())
                    print("")

                else:
                    # Replace cells with ship tile.
                    for position_number in range(start_number, end_number + 1):
                        cell_code = start_position[0] + str(position_number)
                        for (grid_x, grid_y), element in np.ndenumerate(grid):
                            if element == cell_code:
                                grid[grid_x, grid_y] = ship_tile

                    available_ships.remove((end_number - start_number) + 1)

                    clear_screen()
                    


            # Same numbers, different letters
            elif(start_position[1:]) == end_position[1:]:

                start_letter = ord(start_position[0])
                end_letter = ord(end_position[0])

                if(start_letter > end_letter):
                    
                    start_letter, end_letter = reverse_variables(start_letter, end_letter)

                if ((end_letter - start_letter) + 1) not in available_ships:
                    print(ship_length_invalid())
                    print("")

                else:
                    for position_letter in range(start_letter, end_letter + 1):
                        cell_code = chr(position_letter) + start_position[1:]
                        for (grid_x, grid_y), element in np.ndenumerate(grid):
                            if element == cell_code:
                                grid[grid_x, grid_y] = ship_tile

                    available_ships.remove((end_letter - start_letter) + 1)

                    clear_screen()


            else:
                print(ship_placement_invalid_diagonal())
                print("")


def grid_fire(fired_cell, opponent_main_grid, player_top_grid):

    is_game_over = False
    shot_status = ""

    cell_x = int(letters.index(fired_cell[0]))
    cell_y = int(fired_cell[1:])

    if (cell_x > np.size(opponent_main_grid, 0)) or (cell_y > np.size(opponent_main_grid, 1)):
        print(shot_out_of_board())

    else:
        for (grid_x, grid_y), element in np.ndenumerate(opponent_main_grid):

            if (cell_x == grid_x) and (cell_y == grid_y):
                
                if element == fired_cell:
                    opponent_main_grid[grid_x, grid_y] = fire_miss_tile
                    player_top_grid[grid_x, grid_y] = fire_miss_tile

                    shot_status = "Missed"

                elif element == ship_tile:
                    opponent_main_grid[grid_x, grid_y] = ship_hit_tile
                    player_top_grid[grid_x, grid_y] = ship_hit_tile

                    shot_status = "Hit"

                    if ship_tile not in opponent_main_grid:
                        is_game_over = True

                else:
                    shot_status = "Hit Twice"

    return shot_status, is_game_over