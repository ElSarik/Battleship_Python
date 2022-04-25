import os
import numpy as np
import string

from messages import *

from calculations import reverse_variables, cell_to_coordinates


def grid_init():

    size = 10

    list_grid = []
    

    for row in range(size):
        list_grid.append([letters[row] + str(column) for column in range(size)])

    grid = np.array(list_grid)

    return(grid)


def grid_display(grid):
    print(grid)


def ship_placement(grid, available_ships, player):

    while available_ships != []:

        cells = []
        
        grid_display(grid)
        print("")
        print(f"{player} place your ships!")
        print(f"{remaining_ship_sizes()}{available_ships}")
        start_position, end_position = input(enter_ship_coordinates()).split()

        if ((start_position not in grid) or (end_position not in grid)):
            clear_screen()
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
                        cells.append(cell_code)
                        
                    # Check if ship is already placed in the selected tiles.
                    ship_placed = False
                    for cell in cells:
                        cell_row, cell_column = cell_to_coordinates(cell)
                        if grid[cell_row, cell_column] == ship_tile:
                            ship_placed = True
                            
                    if ship_placed == False:
                        for cell in cells:
                            cell_row, cell_column = cell_to_coordinates(cell)
                            grid[cell_row, cell_column] = ship_tile

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
                    # Replace cells with ship tile.
                    for position_letter in range(start_letter, end_letter + 1):
                        cell_code = chr(position_letter) + start_position[1:]
                        cells.append(cell_code)
                    
                    # Check if ship is already placed in the selected tiles.
                    ship_placed = False
                    for cell in cells:
                        cell_row, cell_column = cell_to_coordinates(cell)
                        if grid[cell_row, cell_column] == ship_tile:
                            ship_placed = True
                            
                    if ship_placed == False:
                        for cell in cells:
                            cell_row, cell_column = cell_to_coordinates(cell)
                            grid[cell_row, cell_column] = ship_tile

                        available_ships.remove((end_letter - start_letter) + 1)

                    clear_screen()


            else:
                clear_screen()
                print(ship_placement_invalid_diagonal())
                print("")


def AI_ship_placement(grid, start_position, end_position):

    if ((start_position not in grid) or (end_position not in grid)):
            return "Invalid placement"

    else:

        cells = []
        
        # Same letters, different numbers
        if(start_position[0] == end_position[0]):

            start_number = int(start_position[1:])
            end_number = int(end_position[1:])

            if(start_number > end_number):

                start_number, end_number = reverse_variables(start_number, end_number)

            # Replace cells with ship tile.
            for position_number in range(start_number, end_number + 1):
                cell_code = start_position[0] + str(position_number)
                cells.append(cell_code)
                        
            # Check if ship is already placed in the selected tiles.
            ship_placed = False
            for cell in cells:
                cell_row, cell_column = cell_to_coordinates(cell)
                if grid[cell_row, cell_column] == ship_tile:
                    ship_placed = True
                    return "Invalid placement"
                            
            if ship_placed == False:
                for cell in cells:
                    cell_row, cell_column = cell_to_coordinates(cell)
                    grid[cell_row, cell_column] = ship_tile
                    

        # Same numbers, different letters
        elif(start_position[1:]) == end_position[1:]:

            start_letter = ord(start_position[0])
            end_letter = ord(end_position[0])

            if(start_letter > end_letter):
                    
                start_letter, end_letter = reverse_variables(start_letter, end_letter)

            # Replace cells with ship tile.
            for position_letter in range(start_letter, end_letter + 1):
                cell_code = chr(position_letter) + start_position[1:]
                cells.append(cell_code)
                    
            # Check if ship is already placed in the selected tiles.
            ship_placed = False
            for cell in cells:
                cell_row, cell_column = cell_to_coordinates(cell)
                if grid[cell_row, cell_column] == ship_tile:
                    ship_placed = True
                    return "Invalid placement"
                            
            if ship_placed == False:
                for cell in cells:
                    cell_row, cell_column = cell_to_coordinates(cell)
                    grid[cell_row, cell_column] = ship_tile


        else:
            return "Invalid placement"
            
    return


def grid_fire(fired_cell, opponent_main_grid, player_top_grid):

    is_game_over = False
    shot_status = ""

    cell_row, cell_column = cell_to_coordinates(fired_cell)

    if (cell_row > np.size(opponent_main_grid, 0)) or (cell_column > np.size(opponent_main_grid, 1)):
        print(shot_out_of_board())

    else:
        for (grid_row, grid_column), element in np.ndenumerate(opponent_main_grid):

            if (cell_row == grid_row) and (cell_column == grid_column):
                
                if element == fired_cell:
                    opponent_main_grid[grid_row, grid_column] = fire_miss_tile
                    player_top_grid[grid_row, grid_column] = fire_miss_tile

                    shot_status = "Missed"

                elif element == ship_tile:
                    opponent_main_grid[grid_row, grid_column] = ship_hit_tile
                    player_top_grid[grid_row, grid_column] = ship_hit_tile

                    shot_status = "Hit"

                    if ship_tile not in opponent_main_grid:
                        is_game_over = True

                else:
                    shot_status = "Hit Twice"

    return shot_status, is_game_over