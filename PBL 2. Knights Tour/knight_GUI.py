# Import necessary modules
from timeit import default_timer as timer  # For measuring execution time
from random import randrange  # For generating random numbers
import tkinter as tk
from tkinter import ttk
import sys

# Set a higher recursion limit
# Required for high board sizes as n*n recursive calls are made
sys.setrecursionlimit(3000)

# Define the move pattern for the knight
cx = [-2, -1, 1, 2, -2, -1, 1, 2]  # Possible horizontal moves for the knight
cy = [1, 2, 2, 1, -1, -2, -2, -1]  # Possible vertical moves for the knight

# Initialize two lists to keep track of all the moves taken in order
movesX = []
movesY = []

# Get user input for n (the size of the chessboard)
def get_n():
    n = int(input("Enter a value for N: "))  # Prompt the user to enter a value for N
    if (n < 5):
        print("N must be greater than 4.")  # Check if N is greater than 4, as the knight's tour problem is meaningful for larger boards
        quit()  # Quit the program if N is not valid
    return n

n = get_n()  # Get the user's input for N

# Create an n*n chessboard initialized with zeros
board = [[0 for x in range(n)] for y in range(n)]

# Set the starting position of the knight on the chessboard
x = 0  # Initial x-coordinate for the knight's starting position (can be randomized or user-defined)
y = 0  # Initial y-coordinate for the knight's starting position (can be randomized or user-defined)
board[x][y] = 1  # Set the first move on the board (1 indicates the first move)


# Print chessboard dimensions and starting position
#print("Board size: %dx%d" %(n,n))
#print("Starting position: (%d, %d)" %(x,y))

### SOLUTION CODE ###

# Checks if the queried move is within the limits of the board and
# whether the position has been visited.
# Returns True if the move can be made or returns False if the move cannot be made.
def if_move_valid(x, y):
    if ((x in range(0, n)) & (y in range(0, n))):  # Check if (x, y) is within the board's bounds
        if (board[x][y] == 0):  # Check if the position has not been visited (0 indicates unvisited)
            return True
    else:
        return False

# Finds all possible valid moves from (x, y) according to the knight's move pattern.
# Returns the number of valid moves.
def get_possibilities(x, y):
    count = 0
    for i in range(8):
        next_x = x + cx[i]  # Get the next x-coordinate based on the knight's move pattern
        next_y = y + cy[i]  # Get the next y-coordinate based on the knight's move pattern
        if if_move_valid(next_x, next_y):
            count += 1  # Increment count for each valid move
    return count

# Finds the move with the smallest degree and makes that move. If it can make another move,
# it will call itself recursively until there are no more possible moves to make.
def nextMove(x, y):
    min_degree = (n + 1)  # Initialize min_degree to a value larger than possible degrees
    next_x = 0
    next_y = 0

    for i in range(8):
        adj_x = x + cx[i]  # Get coordinates of adjacent squares
        adj_y = y + cy[i]  # Get coordinates of adjacent squares
        if if_move_valid(adj_x, adj_y):  # Check if the move is unvisited & within the chess board
            degree = get_possibilities(adj_x, adj_y)  # Finds the number of possible moves from each adjacent position
            if (degree < min_degree):  # Compare to the min_degree to iteratively obtain the move with the smallest degree
                min_degree = degree
                next_x = adj_x
                next_y = adj_y

    if (if_move_valid(next_x, next_y)):  # Track the move if it is valid
        board[next_x][next_y] = board[x][y] + 1  # Update the board to indicate the next move
        movesX.append(x)  # Track the x-coordinate of the move
        movesY.append(y)  # Track the y-coordinate of the move
    else:
        return  # Otherwise break the recursion if no valid moves are available
    return nextMove(next_x, next_y)  # Recursive call until there are no more valid moves


# Solution references https://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/

### DRIVER CODE ###

# Attempt to solve the knight's tour problem starting from the given (x, y) position
start = timer()  # Record the start time
nextMove(x, y)  # Call the function to attempt to solve the tour
end = timer()  # Record the end time after the tour is attempted

# Loop through the squares to verify that the tour has been completed
visited_squares = 0
for x in range(n):
    for y in range(n):
        if (board[x][y] != 0):
            visited_squares += 1

# Check if all squares have been visited (tour completed)
if (visited_squares == n * n):
    print("Knight's Tour: Completed")
    print(f"Time taken: {end - start :0.5f} Seconds")  # Calculate and print the time taken to complete the tour
else:
    print("Knight's Tour: Failed to find a tour")
    quit()  # Exit the program if the tour was not completed

# Little inelegant hack for obtaining the last position and adding it to the movesX and movesY lists
# Needed for GUI
for x in range(n):
    for y in range(n):
        if (board[x][y] == n * n):
            movesX.append(x)  # Add the x-coordinate of the last position to movesX
            movesY.append(y)  # Add the y-coordinate of the last position to movesY


### GUI CODE ###

# Initialize Tkinter and set the window title
root = tk.Tk()
root.title("knight_GUI.py")

# Define the window size and square size
WINDOW_SIZE = 800
squareSize = (WINDOW_SIZE - 1) / n  # Adjust the square size to fit the screen by dividing the window size by n

# Create the main frame
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

# Create a canvas for drawing
canvas = tk.Canvas(mainframe, width=WINDOW_SIZE, height=WINDOW_SIZE, background='white')
canvas.grid(column=0, row=0)

# Create an n*n chessboard within the canvas
def draw_board():
    for i in range(n):
        for j in range(n):
            # Determine the color of each square (alternating between white and black)
            col = 'white' if (i + j) % 2 == 0 else 'black'
            # Create a rectangle for each square with the determined color
            canvas.create_rectangle(
                (i * squareSize) + 2, (j * squareSize) + 2,
                (i * squareSize + squareSize) + 2, (j * squareSize + squareSize) + 2,
                fill=col, outline='black')

# Draw text in the center of each grid space showing an integer value representing the turn order
def draw_text():
    for x in range(n):
        for y in range(n):
            # Create text in the center of each square to display the turn order
            canvas.create_text((x * squareSize) + (squareSize / 2) + 2, (y * squareSize) + (squareSize / 2) + 2, text=str(int(board[x][y])))

# Draw n*n nodes in the center of each grid space
def draw_nodes():
    circle_width = squareSize / 6
    for x in range(n):
        for y in range(n):
            # Create circles (nodes) in the center of each square
            canvas.create_oval((x * squareSize) + (squareSize / 2) - (circle_width / 2) + 2, (y * squareSize) + (squareSize / 2) - (circle_width / 2) + 2,
                               (x * squareSize) + (squareSize / 2) + (circle_width / 2) + 2, (y * squareSize) + (squareSize / 2) + (circle_width / 2) + 2,
                               fill='red', outline='blue', width=1)

# Draw a line between each coordinate and its following coordinate
def draw_lines():
    for i in range(0, len(movesX) - 1):
        # Create lines connecting coordinates in the movesX and movesY lists
        canvas.create_line((movesX[i] * squareSize) + (squareSize / 2) + 2, (movesY[i] * squareSize) + (squareSize / 2) + 2,
                           (movesX[i + 1] * squareSize) + (squareSize / 2) + 2, (movesY[i + 1] * squareSize) + (squareSize / 2) + 2,
                           fill='blue', width=1)

# Convert movesX and movesY into a list of tuples and print
print(list(zip(movesX, movesY)))

# Call the functions to draw components on the canvas
draw_board()
#draw_text()
draw_lines()
draw_nodes()

# Start the main loop of the application
root.mainloop()