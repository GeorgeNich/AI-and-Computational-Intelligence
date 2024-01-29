from soloution import minimax
import random

# Class representing the game board. It stores the current state of the game and provides methods to update it.
class Board(object):
    def __init__(self, board):
        # Initialize the board with the given state.
        self.board = board

    def update(self, piles, num):
        # Update the board by removing 'num' objects from the pile at index 'piles'.
        self.board[piles] -= num

    def computerUpdate(self):
        # Update the board state based on the computer's move.
        # It uses the minimax algorithm to determine the best move.
        self.board = minimax(self.board, -float('inf'), float('inf'), True)[1][1]

# Function to check if the player's move is valid.
def isValid(remove, board):
    # Check if the input format is correct and the move is possible given the current board state.
    if not remove or len(remove) != 2: 
        return False
    if remove[0] > 0 and remove[1] >= 0 and remove[1] < len(board) and remove[0] <= board[remove[1]]:
        return True
    return False

# Function to get and validate the player's input.
def getPlayerInput(board):
    while True:
        user_input = input("Player turn (format 'number index'): ")
        try:
            remove = [int(i) for i in user_input.split()]
            if isValid(remove, board):
                # Return the valid move.
                return remove
            else:
                print("Invalid move! Please input again. Format: 'number index', e.g., '1 0'")
        except ValueError:
            print("Invalid format! Use numbers only. Format: 'number index', e.g., '1 0'")

if __name__ == "__main__":

    print("Starting Nim!")
    # Randomly decide the number of piles for the game.
    numofpiles = random.randint(2, 5)
    print('Piles:', numofpiles)

    n = 1
    list = []
    # Initialize the game board with a predetermined pattern of objects in each pile.
    for number in range(0, numofpiles):
        list.append(n)
        n = (2 * n + 1)

    # Create a game board with the generated list of piles.
    game = Board(list)
    print("Game Setup: Each number represents a pile of objects. Remove objects by specifying the number of objects and the pile index.")
    print("Example: To remove 1 object from pile 0, enter '1 0'. The player who removes the last object loses.")

    player_win = True
    # Main game loop
    while True:
        print("Current Piles: %s" % game.board)

        # Handle the player's turn: get input and update the board
        player_remove = getPlayerInput(game.board)
        game.update(player_remove[1], player_remove[0])

        # Check if the game has ended (player loses if they take the last object)
        if sum(game.board) == 0:
            player_win = False
            break
        elif sum(game.board) == 1:
            break

        print("Computer's turn")
        # Handle the computer's turn using the minimax algorithm
        game.computerUpdate()

        # Check if the game has ended after the computer's turn
        if sum(game.board) == 0:
            break
        elif sum(game.board) == 1:
            player_win = False
            break

    # Determine and display the game result
    if player_win:
        print("You won!")
    else:
        print("You lost, the computer won!")
    print("Final Board:", game.board)

# Pause at the end of the script to view the final output
input('Press Enter to exit...')
