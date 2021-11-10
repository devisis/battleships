import random

score = {"player": 0, "cpu": 0}
is_game_over = False


class Battleships:
    """
    Main class for creating CPU and Player boards,
    keeping count of ships and tracking whos turn it is.
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
            print(' '.join(row))

        print("\n")

    def create_ships(self):
        """
        Plot ship locations randomly
        """
        # Plot ships
        for i in range(5):
            rand1 = random.randint(0, 4)
            rand2 = random.randint(0, 4)
            self.create_board[rand1][rand2] = "⛵"
            self.ship_location.append([rand1, rand2])


def guess_location(self, type):
    """
    Player guesses ship location
    """
    # x = input("Please enter row (0-5): ")
    # y = input("Please enter col: ")
    # self.guess.append([x, y])

    # if [x, y] is in self.ship_location:
    #    self.create_board[x][y] = "✅"
    #    scores(player)
    # else:
    #    self.create_board[x][y] = "❎"


def cpu_guess():
    """
    Computer Guesses ship location
    """
    pass


def scores(type):
    """
    Updates when a ship is sunk
    """
    # score[type] += 1
    # print(f"{type} has sunk a ship")


def game_over(type):
    """
    Checks if game is over
    """
    if score[type] == self.total_ships:
        print(f"Game Over! {type} has won the game!")


def main():
    """
    Main game loop
    prints out game board and shows
    user a visual representation of gameplay
    """
    print("Welcome to Battleships!\n")
    print(
        "Object of the game:\n"
        "Guess the co-ordinates of your opponents ships.\n"
        "After hit or miss your turn is over.\n"
        "First player to sink 5 ships wins.\n")
    player = Battleships("player")
    cpu = Battleships("cpu")

    print("your board")
    player.create_ships()
    player.show_board()
    print(player.ship_location)
    print("cpu board")
    cpu.create_ships()
    cpu.show_board()


main()
