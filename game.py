import copy
import random
from grid import *
from messages import *

from calculations import available_directions, AI_placement_calculation

available_ships = [2, 3, 3, 4, 5]
# available_ships = [2]

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

    clear_screen()

    # By default, P1 is active

    p1_player_grid = grid_init()    # Bottom board of P1 (Player's ships)
    p1_opponent_grid = grid_init()  # Top board of P1 (Opponent's empty board)
    p1_available_ships = copy.deepcopy(available_ships)

    p2_player_grid = grid_init()    # Bottom board of P2 (Player's ships)
    p2_opponent_grid = grid_init()  # Top board of P2 (Opponent's empty board)
    p2_available_ships = copy.deepcopy(available_ships)

    player = check_player()
    ship_placement(p1_player_grid, p1_available_ships, player)  # P1 places ships

    change_player() # Player changes, P2 is now active
    clear_screen()

    player = check_player()
    ship_placement(p2_player_grid, p2_available_ships, player)  # P2 places ships


    is_game_over = False
    shot_status = ""

    while True:

        # P1 makes a move
        shot_status, is_game_over = game_flow(shot_status, p1_player_grid, p2_player_grid, p1_opponent_grid)

        if is_game_over == True:
            player = check_player()
            print(game_over(player))

            break
        
        # P2 makes a move
        shot_status, is_game_over = game_flow(shot_status, p2_player_grid, p1_player_grid, p2_opponent_grid)

        if is_game_over == True:
            player = check_player()
            print(game_over(player))

            break
        
    return


def game_flow(shot_status, player_grid, opponent_player_grid, opponent_grid):

    clear_screen()

    # Displaying current player's board
    grid_display(opponent_grid)
    print("====================================================")
    grid_display(player_grid)

    # Displaying the results of previous player's shot (active player = previous)
    if shot_status == "Missed":
        print("")
        print(f"{check_player()}{shot_miss()}")
    elif shot_status == "Hit":
        print("")
        print(f"{check_player()}{shot_hit()}")
    elif shot_status == "Hit Twice":
        print("")
        print(ship_hit_twice())


    change_player() # Active player changes (active player = current)


    print("")
    print(f"Current turn: {check_player()}")
    shot = input(enter_shot_coordinates())

    shot_status, is_game_over = grid_fire(shot, opponent_player_grid, opponent_grid)   # Current player fires

    return shot_status, is_game_over


def player_vs_ai():

    grid = grid_init()

    ships = copy.deepcopy(available_ships)
    directions = ["up", "down", "left", "right"]

    while ships != []:

        cell = (random.choice(random.choice(grid)))
        cell_directions = copy.deepcopy(directions)
        cell_directions = available_directions(cell_directions, grid, cell)

        if cell_directions == []:
            continue
        
        selected_direction = random.choice(cell_directions)
        selected_ship = random.choice(ships)
            
        end_cell = AI_placement_calculation(grid, cell, selected_direction, selected_ship)

        error = AI_ship_placement(grid, cell, end_cell)

        if end_cell == "Invalid placement" or error == "Invalid placement":
            continue
        
        print(cell, end_cell, selected_ship)
        ships.remove(selected_ship)

    grid_display(grid)

    return
