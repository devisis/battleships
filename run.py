import random

score = {"player": 0, "cpu": 0}
is_game_over = False


class Battleships:
    """
    Main class for creating CPU and Player boards,
    keeping count of ships and tracking whos turn it is.
    """

    def __init__(self, player_type):
        self.player_type = player_type
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
        for _ in range(5):
            row = random_int()
            col = random_int()
            self.ship_location.append((row, col))
            if self.player_type == 'player':
                self.create_board[row][col] = "⛵"

    def hit_or_miss(self, row, col):
        """
        Defines whether the co-ordinates inputed will
        equate to a hit or a miss
        """
        self.guess.append((row, col))
        print(self.guess)
        if (row, col) in self.ship_location:
            return True
        else:
            return False


def random_int():
    """
    Returns a random number to use as co-ordinate data
    """
    return random.randint(0, 4)


def guess_location(board):
    """
    Accepts a board in which to guess if its players turn
    then prompt for ship location and guess on cpu board
    else guess random co-ordinates on player board
    """
    global score
    player_guessing = "player" if board.player_type == "cpu" else "cpu"

    if player_guessing == "player":
        row = int(input("Please enter row (0-4): \n"))
        col = int(input("Please enter col (0-4): \n"))
    else:
        row = random_int()
        col = random_int()

    print(f"{player_guessing} has guessed - {row}, {col}")

    if board.hit_or_miss(row, col) == True:
        score[player_guessing] += 1
        if board.player_type == "cpu":
            print(f"{player_guessing} has hit {board.player_type}'s ship! \n")
            board.create_board[row][col] = "✅"
    else:
        print(f"{player_guessing} has missed {board.player_type}'s ship! \n")
        if board.player_type == "cpu":
            board.create_board[row][col] = "❎"


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
    player = Battleships(player_type="player")
    cpu = Battleships(player_type="cpu")

    player.create_ships()
    print("your board")
    player.show_board()
    print(player.ship_location)
    cpu.create_ships()
    print("cpu board")
    cpu.show_board()
    print(cpu.ship_location)
    guess_location(cpu)
    cpu.show_board()
    guess_location(player)
    player.show_board()

main()
