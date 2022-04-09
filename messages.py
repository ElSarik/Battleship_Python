import os

def clear_screen():
    os.system('cls')


def enter_ship_coordinates():
    return "Enter ship coordinates: "

def enter_shot_coordinates():
    return "Enter your shot coordinates: "


def remaining_ship_sizes():
    return "Remaining ship sizes: "


def ship_placement_invalid():
    return "Invalid placement (start, end position)"

def ship_placement_invalid_diagonal():
    return "Invalid placement (diagonal placement)"


def ship_length_invalid():
    return "Invalid ship length!"

def ship_hit_twice():
    return "Invalid cell! (You have already hit this cell)"


def shot_out_of_board():
    return "Your shot was out of the board!"

def shot_miss():
    return "You missed!"

def shot_hit():
    return "Ship Hit!"


def game_over(player):
    return f"Game over! {player} wins!"