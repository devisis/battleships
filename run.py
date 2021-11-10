import random

score = {"player": 0, "cpu": 0} 
game_over = False

class Battleships:
    """
    Main class for creating CPU and Player boards, keeping count of ships and tracking whos turn it is.
    """

    def __init__(self, type):
        self.type = type
        self.create_board = [["🌊"for x in range(1, 6)] for y in range(1, 6)]
        self.guess = []
        self.ship_location = []
        self.total_ships = 5
 
    def show_board(self):
        """
        Display board
        """
        for row in self.create_board:
            print(" ".join(row))

        # Plot ships
        #for i in range(5):
            #row = random.randint(0, 6)
            #col = random.randint(0, 6)
            #board_list[row][col] = "⛵"

       
    


def create_ships():
    """
    Plot ship locations randomly
    """


def guess_location():
    """
    Player guesses ship location
    """
   # x = input("Please enter row (0-5): ")
   # y = input("Please enter col: ")

   # if board_list[x][y] is "⛵":
    #    board_list[x][y] = "✅"
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

def game_over():
    """
    Checks if game is over
    """
    pass

def main():
    """
    Main game loop
    """

player1 = Battleships("player1")
print(player1.show_board())