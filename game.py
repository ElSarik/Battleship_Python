import os
import copy
from grid import grid_init, grid_display, ship_placement, grid_fire
from messages import *


# available_ships = [2, 3, 3, 4, 5]
available_ships = [2]

player1_active = True


def change_player():
    global player1_active
    
    player1_active = not player1_active


def check_player():

    if player1_active == True:
        return("Player 1")
    else:
        return("Player 2")


def player_vs_player():

    p1_player_grid = grid_init()    # Bottom board of P1 (Player's ships)
    p1_opponent_grid = grid_init()  # Top board of P1 (Opponent's empty board)
    p1_available_ships = copy.deepcopy(available_ships)

    p2_player_grid = grid_init()    # Bottom board of P2 (Player's ships)
    p2_opponent_grid = grid_init()  # Top board of P2 (Opponent's empty board)
    p2_available_ships = copy.deepcopy(available_ships)

    print(check_player())
    ship_placement(p1_player_grid, p1_available_ships)

    change_player()

    print(check_player())
    ship_placement(p2_player_grid, p2_available_ships)

    print("================================")

    change_player()

    is_game_over = False

    while True:

        os.system('cls')

        grid_display(p1_opponent_grid)
        print("==================")
        grid_display(p1_player_grid)

        shot = input(enter_shot_coordinates())

        is_game_over = grid_fire(shot, p2_player_grid, p1_opponent_grid)

        if is_game_over == True:
            player = check_player()
            print(game_over(player))

            break


        change_player()


        os.system('cls')

        grid_display(p2_opponent_grid)
        print("==================")
        grid_display(p2_player_grid)

        shot = input(enter_shot_coordinates())

        is_game_over = grid_fire(shot, p1_player_grid, p2_opponent_grid)

        if is_game_over == True:
            player = check_player()
            print(game_over(player))

            break

        change_player()

    return