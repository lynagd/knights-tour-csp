from src.heuristics import KnightCSPHeuristics, successor_fct
import time
import sys


def backtracking(assignment, heuristics):
    #Backtracking algorithm with MRV and LCV heuristics
   
    # Track progress
    heuristics.nodes_explored += 1
    
    # Progress indicator
    if heuristics.nodes_explored % 50 == 0:
        print(f"  Progress: {len(assignment)}/64 | Nodes: {heuristics.nodes_explored}", end='\r')
    
    # Safety check
    if heuristics.nodes_explored > 10000:
        print(f"\n Warning: Explored {heuristics.nodes_explored} nodes. Something may be wrong.")
        print("   Stopping search...")
        return None
    
    # BASE CASE: All 64 squares visited
    if len(assignment) == 64:
        return assignment
    
    # Get current position
    current_x, current_y = assignment[-1]
    
    # Get visited set
    visited = set(assignment)
    
    # Get valid successors
    successors = successor_fct(current_x, current_y, visited)
    
    # If no successors, dead end
    if not successors:
        return None
    
    # MRV and LCV heuristics 
    successors = heuristics.apply_heuristics(successors, visited)
    
    # Try each successor
    for x, y in successors:
        # Make move
        assignment.append((x, y))
        
        # Recursive call
        result = backtracking(assignment, heuristics)
        
        # If solution found, return it
        if result is not None:
            return result
        
        # Backtrack
        assignment.pop()
    
    # No solution found
    return None


def solve_knights_tour():
    print("=" * 70)
    print("KNIGHT'S TOUR - CSP BACKTRACKING WITH MRV & LCV HEURISTICS")
    print("=" * 70)
    print(f"Board size: 8x8 (64 squares)")
    print(f"Starting position: (0, 0)")
    print(f"Heuristics: MRV + LCV ")
    print("=" * 70)
    print()
    
    # Create heuristics instance
    heuristics = KnightCSPHeuristics(board_size=8)
    
    # Initial assignment
    assignment = [(0, 0)]
    
    print("🔍 Searching for solution...")
    print()
    
    # Solve
    start_time = time.time()
    solution = backtracking(assignment, heuristics)
    end_time = time.time()
    
    time_taken = end_time - start_time
    nodes = heuristics.nodes_explored
    
    print()  # Clear progress line
    
    if solution:
        print("=" * 70)
        print("SOLUTION FOUND!")
        print("=" * 70)
        print(f"Path length: {len(solution)} squares")
        print(f"Time taken: {time_taken:.4f} seconds")
        print(f"Nodes explored: {nodes:,}")
        if time_taken > 0:
            print(f"Search speed: {int(nodes/time_taken):,} nodes/second")
        print()
        print(f"First 10 moves: {solution[:10]}")
        print(f"Last 10 moves: {solution[-10:]}")
        print("=" * 70)
        
        return solution, time_taken, nodes
    else:
        print("=" * 70)
        print(" NO SOLUTION FOUND (or stopped early)")
        print("=" * 70)
        print(f"Time taken: {time_taken:.4f} seconds")
        print(f"Nodes explored: {nodes:,}")
        print("=" * 70)
        
        return None, time_taken, nodes


def print_board(solution):
    if not solution:
        return
    
    board = [[0 for _ in range(8)] for _ in range(8)]
    
    for move_num, (x, y) in enumerate(solution):
        board[x][y] = move_num + 1
    
    print("\n" + "=" * 70)
    print("SOLUTION BOARD (Move Numbers)")
    print("=" * 70)
    print("\n     ", end="")
    for i in range(8):
        print(f" {i:2d} ", end="")
    print("\n   +" + "----+" * 8)
    
    for i in range(8):
        print(f" {i} |", end="")
        for j in range(8):
            print(f" {board[i][j]:2d} |", end="")
        print()
        print("   +" + "----+" * 8)
    print()


def verify_solution(solution):
    #Verify that the solution is valid
    if not solution or len(solution) != 64:
        print(f" Invalid length: {len(solution) if solution else 0}/64")
        return False
    
    if len(set(solution)) != 64:
        print(" Duplicate positions found")
        return False
    
    KNIGHT_MOVES = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]
    
    for i in range(len(solution)):
        x, y = solution[i]
        
        if not (0 <= x < 8 and 0 <= y < 8):
            print(f"❌ Position {i}: {solution[i]} is out of bounds")
            return False
        
        if i > 0:
            prev_x, prev_y = solution[i-1]
            dx, dy = x - prev_x, y - prev_y
            
            if (dx, dy) not in KNIGHT_MOVES:
                print(f"❌ Invalid move from {solution[i-1]} to {solution[i]}")
                return False
    
    print(" Solution is VALID!")
    print("   - All 64 squares visited")
    print("   - All positions unique")
    print("   - All knight moves valid")
    print("   - All positions within bounds")
    
    return True


def main():
    print("\n" + "█" * 70)
    print("█" + " " * 68 + "█")
    print("█" + " " * 10 + "KNIGHT'S TOUR - CSP WITH MRV & LCV HEURISTICS" + " " * 14 + "█")
    print("█" + " " * 68 + "█")
    print("█" * 70)
    print()
    
    # Solve
    solution, time_taken, nodes = solve_knights_tour()
    
    if solution:
        # Display board
        print_board(solution)
        
        # Verify
        print("\n" + "=" * 70)
        print("SOLUTION VERIFICATION")
        print("=" * 70)
        verify_solution(solution)
        print("=" * 70)
        
        # Performance summary
        print("\n" + "=" * 70)
        print("PERFORMANCE SUMMARY")
        print("=" * 70)
        print(f"✓ Solution found in {time_taken:.4f} seconds")
        print(f"✓ Explored only {nodes:,} nodes")
        print(f"✓ Heuristics reduced search space effectively!")
        print("=" * 70)
    else:
        print("\n If the search stopped early (>10,000 nodes), the heuristics")
    
    print("\n" + "█" * 70)
    print("█" + " " * 68 + "█")
    print("█" + " " * 28 + "COMPLETE!" + " " * 30 + "█")
    print("█" + " " * 68 + "█")
    print("█" * 70 + "\n")


if __name__ == "__main__":
    main()