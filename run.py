import random

score = {"player": 0, "cpu": 0} 
game_over = False

class Battleships:
    """
    Main class for creating CPU and Player boards, keeping count of ships and tracking whos turn it is.
    """

    def __init__(self, type):
        self.type = type
        self.create_board = [["🌊"for x in range(5)] for y in range(5)]
        self.guess = []
        self.ship_location = []
        self.total_ships = 5
 
    def show_board(self):
        """
        Display board
        """
        for row in self.create_board:
            print(" ".join(row))
     
    def create_ships(self):
        """
        Plot ship locations randomly
        """
        # Plot ships
        for i in range(5):
            rand1 = random.randint(0, 4)
            rand2 = random.randint(0, 4)
            self.create_board[rand1][rand2] = "⛵"

def guess_location(self, type):
    """
    Player guesses ship location
    """
   # x = input("Please enter row (0-5): ")
   # y = input("Please enter col: ")

   # if board_list[x][y] is "⛵":
    #    board_list[x][y] = "✅"
    #    score[type] += 1
    #else:
     #   board_list[x][y] = "❎"


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

def game_over(type):
    """
    Checks if game is over
    """
    if score[type] == self.total_ships:
        print(f"Game Over! {type} has won the game!")

def main():
    """
    Main game loop
    """

player = Battleships("player")
player.create_ships()
player.show_board()