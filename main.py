from grid import grid_display, grid_init, ship_placement

def main():
    
    grid = grid_init()

    ship_placement("A2", "A4")
    # print("============")
    ship_placement("B6", "G6")

    grid_display()


if __name__ == "__main__":
    main()