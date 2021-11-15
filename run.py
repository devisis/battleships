import random

SCORE = {"player": 0, "cpu": 0}
IS_GAME_OVER = False
ALPHABET = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
    "F": 5, "G": 6, "H": 7, "I": 8, "J": 9
}
DOTEDLINE = "-" * 40


class Battleships:
    """
    Main class for creating CPU and Player boards,
    keeping count of ships and tracking whos turn it is.
    """

    def __init__(self, size, player_type):
        self.size = size
        self.player_type = player_type
        self.create_board = [["🌊" for x in range(size)] for y in range(size)]
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
        for _ in range(5):
            row = random_int(self.size)
            col = random_int(self.size)
            self.ship_location.append((row, col))
            if self.player_type == "player":
                self.create_board[row][col] = "⛵"

    def hit_or_miss(self, row, col):
        """
        Defines whether the co-ordinates inputed will
        equate to a hit or a miss
        """
        self.guess.append((row, col))
        if (row, col) in self.ship_location:
            return True
        else:
            return False


def random_int(size):
    """
    Returns a random number to use as co-ordinate data
    """
    return random.randint(0, size - 1)


def guess_location(board):
    """
    Accepts a board in which to guess if its players turn
    then prompt for ship location and guess on cpu board
    else guess random co-ordinates on player board
    """
    global SCORE
    global IS_GAME_OVER
    player_guessing = "player" if board.player_type == "cpu" else "cpu"
    if not IS_GAME_OVER:
        if player_guessing == "player":
            row = int(input("Please enter row (A):\n"))
            col = int(input(f"Please enter col (0 - {board.size - 1}):\n"))
            print(DOTEDLINE)
        else:
            row = random_int(board.size)
            col = random_int(board.size)

        print(f"{player_guessing} has guessed {row}, {col}...")
        print(DOTEDLINE)

        if board.hit_or_miss(row, col):
            SCORE[player_guessing] += 1
            print(f"{player_guessing} hit {board.player_type}'s ships!\n")
            if board.player_type == "cpu":
                board.create_board[row][col] = "🔥"
        else:
            print(f"{player_guessing} missed {board.player_type}'s ships!\n")
            if board.player_type == "cpu":
                board.create_board[row][col] = "❎"

        print(player_guessing, board.guess)
        print(SCORE[player_guessing])

        if SCORE[player_guessing] == 5:
            IS_GAME_OVER = True
            print(DOTEDLINE)
            print(f"The game is over! {player_guessing} has won the game!")
            print(DOTEDLINE)
            print(DOTEDLINE)


def val_board_size():


def val-coordinates():


def main():
    """
    Main game loop
    prints out game board and shows
    user a visual representation of gameplay
    """
    global IS_GAME_OVER

    print("=" * 40)
    print("Welcome to Battleships!")
    print("=" * 40)
    print("Object of the game:")
    print(DOTEDLINE)
    print(
        "Guess the co-ordinates of your opponents ships.\n"
        "After hit - 🔥  or miss - ❎ your turn is over.\n"
        "First player to sink 5 ships wins.")
    print(DOTEDLINE)

    size = int(input("Please enter board size from 5-10: "))
    print(DOTEDLINE)

    player = Battleships(size, player_type="player")
    cpu = Battleships(size, player_type="cpu")

    player.create_ships()
    cpu.create_ships()

    while not IS_GAME_OVER:
        print(DOTEDLINE)
        print("your board")
        print(DOTEDLINE)
        player.show_board()
        print(DOTEDLINE)
        print("cpu board")
        print(DOTEDLINE)
        cpu.show_board()
        print(cpu.ship_location)
        print(DOTEDLINE)
        guess_location(cpu)
        print(DOTEDLINE)
        guess_location(player)
        print(DOTEDLINE)


main()
