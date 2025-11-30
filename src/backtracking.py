# backtracking.py

from csp import successor_fct  # Import our helper function from csp.py


def backtracking(assignment):
    """
    This is the RECURSIVE backtracking algorithm.
    It tries to find a complete knight's tour.
    
    Parameters:
    assignment: a list of positions the knight has visited so far
                Example: [(0,0), (1,2), (3,3), ...]
    
    Returns:
    The complete solution (list of 64 positions) if found, or None if no solution exists
    """
    
    # BASE CASE: Are we done?
    # If we've visited 64 squares (all squares on the 8x8 board), we found a solution!
    if len(assignment) == 64:
        return assignment  # Success! Return the complete tour
    
    # If we're not done yet, we need to find the next move...
    
    # Step 1: Get the knight's current position (the last position in our list)
    current_x, current_y = assignment[-1]  # -1 means "last item in the list"
    
    # Step 2: Create a SET of visited positions (sets are faster for checking "is this in there?")
    visited = set(assignment)  # Convert list to set for faster lookup
    
    # Step 3: Find all valid next moves from current position
    successors = successor_fct(current_x, current_y, visited)
    
    # Step 4: Try each possible next move one by one
    for x, y in successors:
        # Try this move: add it to our path
        assignment.append((x, y))
        
        # RECURSION: Call backtracking again with this new move added
        # This explores deeper: "Can we complete the tour from here?"
        result = backtracking(assignment)
        
        # Did we find a complete solution?
        if result is not None:
            return result  # Yes! Pass the solution up the chain
        
        # If we reach here, that move didn't work out (dead end)
        # BACKTRACK: Remove the move we just tried
        assignment.pop()  # Remove last item from list
    
    # If we tried all successors and none worked, return None (failure)
    return None


def solve_knights_tour():
    """
    This is a helper function that sets up and solves the knight's tour.
    
    Returns:
    The solution path (list of 64 positions) or None if no solution
    """
    
    # Start the knight at position (0, 0) - top left corner
    assignment = [(0, 0)]
    
    # Call the backtracking function to find the solution
    solution = backtracking(assignment)
    
    return solution