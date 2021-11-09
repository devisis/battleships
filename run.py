import random

score = {"player": 0, "cpu": 0} 
game_over = False

def board():
    """
    Create game board
    """
    
    board_list = []
    for x in range(1, 6):
        row = []
        board_list.append(row)
        for y in range(1, 6):
            row.append("🌊")

    for row in board_list:
        print(" ".join(row))
            


def create_ships():
    """
    Plot ship locations randomly
    """
    pass

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

board()