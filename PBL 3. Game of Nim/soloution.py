# This code implements the Minimax algorithm with Alpha-Beta pruning for decision-making in games.

def minimax(position, alpha, beta, maxPlayer):
    """
    Minimax function to decide the best move based on the current game state.
    It recursively evaluates all possible moves and chooses the optimal one.

    Args:
    position: Current state of the game (e.g., board configuration).
    alpha: The best already explored option along the path for the maximizer.
    beta: The best already explored option along the path for the minimizer.
    maxPlayer: Boolean indicating if it's the maximizer's turn.

    Returns:
    A tuple containing the evaluation of the position and the resulting position.
    """
    
    # Base cases for the recursion - determining the final state of the game.
    # Returns -1 if it's a losing state for the current player, 1 for a winning state.
    if (sum(position) == 1 and maxPlayer) or (sum(position) == 0 and not maxPlayer):
        return (-1, [position])
    if (sum(position) == 1 and not maxPlayer) or (sum(position) == 0 and maxPlayer):
        return (1, [position])
    
    # Maximizing player's turn
    if maxPlayer:
        maximumEvaluation = -float('inf')  # Worst evaluation for maximizer
        result = None
        for i in find_next(position):
            # Recursively search for the next possible move
            val, temp = minimax(i, alpha, beta, False)
            if val > maximumEvaluation:
                maximumEvaluation = val
                result = temp
            alpha = max(alpha, val)  # Update the upper bound for Alpha
            if alpha >= beta:  # Alpha-Beta pruning
                break
        return maximumEvaluation, [position] + result
    # Minimizing player's turn
    else:
        minimumEvaluation = float('inf')  # Worst evaluation for minimizer
        result = None
        for i in find_next(position):
            val, temp = minimax(i, alpha, beta, True)
            if val < minimumEvaluation:
                minimumEvaluation = val
                result = temp
            beta = min(beta, val)  # Update the lower bound for Beta
            if alpha >= beta:  # Alpha-Beta pruning
                break
        return minimumEvaluation, [position] + result

def find_next(position):
    """
    Generate all possible next moves from the current position.

    Args:
    position: The current state of the game.

    Returns:
    A list of all possible next moves.
    """
    visited = set()  # To avoid revisiting the same state
    res = []  # List to store next possible moves

    # Iterate through each pile
    for i in range(len(position)):
        # Generate new positions by removing 1 to m objects from the pile
        for m in range(1, position[i] + 1):
            temp = list(position[:])
            temp[i] -= m
            rearranged = tuple(sorted(temp))  # Sort to handle duplicate states
            if rearranged not in visited:
                res.append(temp)  # Append if this state has not been visited
                visited.add(rearranged)

    return res
