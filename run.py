import random

SCORE = {"player": 0, "cpu": 0}
IS_GAME_OVER = False
# ALPH = {
#     "A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
#     "F": 5, "G": 6, "H": 7, "I": 8, "J": 9
# }
DOTEDLINE = "-" * 50


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
        self.total_ships = 0

    def show_board(self):
        """
        Display board
        """

        for row in self.create_board:
            print(" ".join(row))

    def create_ships(self):
        """
        Plot ship locations randomly
        If co-ordinates are already on the board try again
        Plot until you have 5 unique ships
        """
        # Plot ships
        while self.total_ships < 5:
            row = random_int(self.size)
            col = random_int(self.size)

            if (col, row) in self.ship_location:
                continue
            else:
                self.ship_location.append((col, row))
                self.total_ships += 1

            if self.player_type == "player":
                self.create_board[col][row] = "⛵"

    def hit_or_miss(self, col, row):
        """
        Defines whether the co-ordinates inputed will
        equate to a hit or a miss
        """
        self.guess.append((col, row))
        if (col, row) in self.ship_location:
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
    Checks board type to see whos turn it is
    If players turn accept co-ordinates and check if valid
    If valid place on board with relevant icon
    if cpu turn guess random co-ordinates on player board
    then plot relevant icon
    if score = 5 all opposition ships are taken and game is over
    """
    global SCORE
    global IS_GAME_OVER
    valid = False
    # pos = list(ALPH.keys())[list(ALPH.values()).index(board.size - 1)]
    player_guessing = "player" if board.player_type == "cpu" else "cpu"

    if player_guessing == "player":
        while not valid:
            try:
                # col = int(input(f"Please enter col (A - {pos}):\n"))
                col = int(input(f"Enter a column (0 - {board.size - 1}):\n"))
                row = int(input(f"Enter a row (0 - {board.size - 1}):\n"))
                val_check = val_coord(board, col, row)
                print(DOTEDLINE)
                if val_check == "Valid":
                    valid = True
                elif val_check == "Duplicate":
                    print("You've guessed this already, try again!")
                    print(DOTEDLINE)
                elif val_check == "Out":
                    print("Out of board, try again!")
                    print(DOTEDLINE)
            except ValueError:
                print("Error, enter a number!")
                valid = False

    else:
        while not valid:
            col = random_int(board.size)
            row = random_int(board.size)
            val_cpu_check = cpu_val(board, col, row)
            if val_cpu_check == "Duplicate":
                valid = False
            elif val_cpu_check == "Valid":
                valid = True

    print(f"{player_guessing} has guessed column: {col} and row: {row} ...")
    print(DOTEDLINE)

    if board.hit_or_miss(col, row):
        SCORE[player_guessing] += 1
        print(f"{player_guessing} hit {board.player_type}'s ship!")
        board.create_board[col][row] = "🔥"
        board.ship_location.remove((col, row))
    else:
        print(f"{player_guessing} missed {board.player_type}'s ships!")
        if board.player_type == "cpu":
            board.create_board[col][row] = "❌"
    # print(f"{player_guessing} guesses so far: {board.guess}")


def val_board_size(size):
    """
    Board size validation
    Returns Less if less than range
    Returns More if greater than range
    Returns valid if valid
    """
    if size < 5:
        return "Less"
    elif size > 10:
        return "More"
    return "valid"


def val_coord(board, col, row):
    """
    Coordinate validation
    Returns out if guess is out of board scope
    Returns duplicate if guess has been made already
    Returns valid if guess is valid
    """
    if (row > board.size - 1 or row < 0) or (col < 0 or col > board.size - 1):
        return "Out"
    elif (col, row) in board.guess:
        return "Duplicate"
    return "Valid"


def cpu_val(board, col, row):
    if (col, row) in board.guess:
        return "Duplicate"
    else:
        return "Valid"


def game_over(player, cpu):
    """
    Stops the game one 5 ships have been sunk
    Print statements regarding win, loss or draw are set here also
    """
    global IS_GAME_OVER

    if player.ship_location and cpu.ship_location:
        print(f"\nShips hit - Player: {SCORE['player']} CPU: {SCORE['cpu']}\n")
    else:
        IS_GAME_OVER = True
        print(f"\nShips hit - Player: {SCORE['player']} CPU: {SCORE['cpu']}\n")
        if not cpu.ship_location and not player.ship_location:
            print(DOTEDLINE)
            print("The game is over! Draw!")
            print(f"{DOTEDLINE}\n")
        elif player.ship_location and not cpu.ship_location:
            print("⋆" * 50)
            print("The game is over! You have won the game!")
            print("⋆" * 50)
        elif not player.ship_location and cpu.ship_location:
            print(DOTEDLINE)
            print("Game Over - You lost, better luck next time!")
            print(f"{DOTEDLINE}\n")


def main():
    """
    Main game loop
    Prints out game board and shows
    User a visual representation of gameplay
    """
    global IS_GAME_OVER
    valid = False
    print(

        "                     __/___\n"
        "               _____/______|\n"
        "       _______/_____\_______\_____\n"
        "       \  devisis     < < <       |\n"
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        )
    print("~" * 50)
    print("Welcome to Battleships!")
    print("=" * 50)
    print("Object of the game:\n")
    print(
        "Guess the co-ordinates of your opponents ships.\n"
        "After hit - 🔥  or miss - ❌ your turn is over.\n"
        "First player to sink 5 ships wins.")
    print(DOTEDLINE)
    while not valid:
        try:
            size = int(input("Please enter board size from 5 - 10: "))
            board_check = val_board_size(size)
            if board_check == "valid":
                valid = True
            if board_check == "Less":
                print("Too small - Choose a size between 5 and 10")
                print(DOTEDLINE)
            if board_check == "More":
                print("Too big - Choose a size between 5 and 10")
                print(DOTEDLINE)
        except ValueError:
            print("Error - Please enter a number")
            valid = False

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
        print(DOTEDLINE)
        guess_location(cpu)
        print(DOTEDLINE)
        guess_location(player)
        print(DOTEDLINE)
        game_over(player, cpu)
    if input("\nPlay again? enter 'y' to start a new game: \n").lower() == "y":
        IS_GAME_OVER = False
        main()
    else:
        print("Thanks for playing see you later!\n")


main()
