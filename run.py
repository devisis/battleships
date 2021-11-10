import random

score = {"player": 0, "cpu": 0} 
game_over = False

def create_board():
    """
    Create game board
    """
    board_list = []
    for x in range(1, 6):
        row = []
        board_list.append(row)
        for y in range(1, 7):
            row.append("🌊")

    # Plot ships
    for i in range(5):
        row = random.randint(1, 4)
        col = random.randint(1, 4)
        board_list[row][col] = "⛵"

    for row in board_list:
        print(" ".join(row))
    


def create_ships():
    """
    Plot ship locations randomly
    """


def guess_location():
    """
    Player guesses ship location
    """

def cpu_guess():
    """
    Computer Guesses ship location
    """
    pass

def scores():
    """
    Updates when a ship is sunk
    """
    pass

def game_over():
    """
    Checks if game is over
    """
    pass

def main():
    """
    Main game loop
    """

create_board()