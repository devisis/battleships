import random

score = {"player": 0, "cpu": 0} 
game_over = False

class Battleships:
    def __init__(self, create_board, total_ships, type):
        self.create_board = []
        self.total_ships = total_ships
        self.type = type
        self.guess = []
        self.ship_location = []
        

    def show_board():
        """
        Create game board
        """
        board_list = []
        for x in range(1, 6):
            row = []
            board_list.append(row)
            for y in range(1, 6):
                row.append("🌊")

        # Plot ships
        for i in range(5):
            row = random.randint(0, 6)
            col = random.randint(0, 6)
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
    x = input("Please enter row (0-5): ")
    y = input("Please enter col: ")

    if board_list[x][y] is "⛵":
        board_list[x][y] = "✅"
    else:
        board_list[x][y] = "❎"


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