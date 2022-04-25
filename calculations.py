import random

from messages import *

def reverse_variables(first_variable, second_variable):
    return second_variable, first_variable


def cell_to_coordinates(cell):

    cell_row = int(letters.index(cell[0]))
    cell_column = int(cell[1:])

    return cell_row, cell_column


def coordinates_to_cell(cell_row, cell_column):
    cell_letter = letters[cell_row]
    cell = str(cell_letter) + str(cell_column)

    return cell


def available_directions(directions, grid, cell):

    if cell != ship_tile:
        grid_rows = len(grid)
        grid_cols = len(grid[0])

        cell_row, cell_column = cell_to_coordinates(cell)

        if cell == grid[0][0]:
            directions.remove("up")
            directions.remove("left")

        elif cell == grid[0][grid_cols - 1]:
            directions.remove("up")
            directions.remove("right")

        elif cell == grid[grid_rows - 1][0]:
            directions.remove("down")
            directions.remove("left")

        elif cell == grid[grid_rows - 1][grid_cols - 1]:
            directions.remove("down")
            directions.remove("right")

        if ((cell_row == 0 or cell_row - 1 == ship_tile) and "left" in directions):
            directions.remove("left")

        if ((cell_row == grid_cols - 1 or cell_row + 1 == ship_tile) and "right" in directions):
            directions.remove("right")

        if ((cell_column == 0 or cell_column - 1 == ship_tile) and "up" in directions):
            directions.remove("up")

        if ((cell_column == grid_rows - 1 or cell_row + 1 == ship_tile) and "down" in directions):
            directions.remove("down")
    else:
        directions = []

    return directions


def AI_placement_calculation(grid, start_cell, direction, ship_size):

    grid_rows = len(grid)
    grid_cols = len(grid[0])

    cell_row, cell_column = cell_to_coordinates(start_cell)

    if direction == "up":

        end_cell_row = (cell_row + 1) - ship_size
        if end_cell_row < 0:
            return "Invalid placement"
        else:
            end_cell = coordinates_to_cell(end_cell_row, cell_column)


    elif direction == "down":
        end_cell_row = (cell_row - 1) + ship_size
        if end_cell_row > grid_rows:
            return "Invalid placement"
        else:
            end_cell = coordinates_to_cell(end_cell_row, cell_column)


    elif direction == "left":
        end_cell_column = (cell_column + 1) - ship_size
        if end_cell_column < 0:
            return "Invalid placement"
        else:
            end_cell = coordinates_to_cell(cell_row, end_cell_column)


    elif direction == "right":
        end_cell_column = (cell_column - 1) + ship_size
        if end_cell_column > grid_cols:
            return "Invalid placement"
        else:
            end_cell = coordinates_to_cell(cell_row, end_cell_column)

    return end_cell