# csp.py

def get_knight_moves(x, y):
    """
    This function returns all 8 possible L-shaped moves a knight can make.
    
    Parameters:
    x: current row position (0-7)
    y: current column position (0-7)
    
    Returns:
    A list of tuples representing all possible positions the knight could move to
    """
    moves = [
        (x + 2, y + 1),  # Move 2 down, 1 right
        (x + 2, y - 1),  # Move 2 down, 1 left
        (x - 2, y + 1),  # Move 2 up, 1 right
        (x - 2, y - 1),  # Move 2 up, 1 left
        (x + 1, y + 2),  # Move 1 down, 2 right
        (x + 1, y - 2),  # Move 1 down, 2 left
        (x - 1, y + 2),  # Move 1 up, 2 right
        (x - 1, y - 2)   # Move 1 up, 2 left
    ]
    
    return moves


def is_valid_position(x, y):
    """
    Check if a position is inside the 8x8 chessboard, so from 0 to 7.
    
    Parameters:
    x: row position
    y: column position
    
    Returns:
    True if position is valid (inside board), False otherwise
    """
    return 0 <= x < 8 and 0 <= y < 8


def successor_fct(current_x, current_y, visited):
    """
    This is THE MOST IMPORTANT function!
    It finds all valid next moves for the knight.
    
    Parameters:
    current_x: knight's current row
    current_y: knight's current column
    visited: a set of positions already visited (so we don't go there again)
    
    Returns:
    A list of valid next positions (tuples)
    """
    
    # Step 1: Get all 8 possible knight moves from current position
    possible_moves = get_knight_moves(current_x, current_y)
    
    # Step 2: Create an empty list to store only the VALID moves
    valid_successors = []
    
    # Step 3: Check each possible move one by one
    for move in possible_moves:
        x, y = move  # Extract the x and y from the move tuple
        
        # Check THREE things (these are our constraints!):
        # 1. Is the position inside the board? (use is_valid_position)
        # 2. Have we NOT visited this position before? (check if move is NOT in visited set)
        if is_valid_position(x, y) and move not in visited:
            # If both conditions are true, this is a valid move!
            valid_successors.append(move)
    
    # Step 4: Return all the valid moves
    return valid_successors