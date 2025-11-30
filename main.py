# main.py

import time  # To measure how long the algorithm takes
from backtracking import solve_knights_tour  # Import our solver


def print_board(solution):
    """
    Visualize the knight's tour on an 8x8 board.
    Shows the ORDER in which squares were visited (0 to 63).
    
    Parameters:
    solution: list of 64 positions representing the knight's path
    """
    
    # Create an 8x8 board filled with -1 (meaning "not visited yet")
    board = [[-1 for _ in range(8)] for _ in range(8)]
    
    # Fill in the board with the move numbers
    for move_number, (x, y) in enumerate(solution):
        board[x][y] = move_number  # Put the move number at position (x, y)
    
    # Print the board
    print("\nKnight's Tour Solution:")
    print("=" * 50)
    
    for row in board:
        # Print each number with 2 digits (so they line up nicely)
        print(" ".join(f"{num:2}" for num in row))
    
    print("=" * 50)


def print_path(solution):
    """
    Print the path as a sequence of positions.
    
    Parameters:
    solution: list of 64 positions
    """
    print("\nPath taken by the knight:")
    print("-" * 50)
    
    for i, (x, y) in enumerate(solution):
        # Print: Move 0: (0, 0)
        print(f"Move {i}: ({x}, {y})")
    
    print("-" * 50)


def main():
    """
    Main function that runs everything!
    """
    
    print("🐴 Starting Knight's Tour Solver (Basic Backtracking)...")
    print()
    
    # Record the start time
    start_time = time.time()
    
    # Solve the knight's tour!
    solution = solve_knights_tour()
    
    # Record the end time
    end_time = time.time()
    
    # Calculate how long it took
    elapsed_time = end_time - start_time
    
    # Check if we found a solution
    if solution:
        print("✅ Solution found!")
        print(f"⏱️  Time taken: {elapsed_time:.4f} seconds")
        print(f"📊 Total moves: {len(solution)}")
        
        # Display the solution
        print_board(solution)
        
        # Optionally print the full path (might be long!)
        print_path_choice = input("\nDo you want to see the full path? (y/n): ")
        if print_path_choice.lower() == 'y':
            print_path(solution)
    else:
        print("❌ No solution found!")
    
    print("\n🏁 Program finished!")


# This is the entry point of the program
# When you run "python main.py", this code executes
if __name__ == "__main__":
    main()