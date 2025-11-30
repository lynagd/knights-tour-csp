class KnightCSPHeuristics:
    # Define the 8 possible L-shaped knight moves
    KNIGHT_MOVES = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]
    
    def __init__(self, board_size=8):
        
        self.board_size = board_size
        self.nodes_explored = 0
    
    def get_legal_moves(self, x, y, visited):
        #Get all legal knight moves from position (x, y)
       
        legal_moves = []
        
        for dx, dy in self.KNIGHT_MOVES:
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < self.board_size and 0 <= new_y < self.board_size:
                if (new_x, new_y) not in visited:
                    legal_moves.append((new_x, new_y))
        
        return legal_moves
    
    def count_onward_moves(self, x, y, visited):
        #Count the number of legal moves available from position (x, y)
        
        # Create temporary visited set that includes this position
        temp_visited = visited | {(x, y)}
        
        # Count legal moves
        count = 0
        for dx, dy in self.KNIGHT_MOVES:
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < self.board_size and 0 <= new_y < self.board_size:
                if (new_x, new_y) not in temp_visited:
                    count += 1
        
        return count
    
    def apply_heuristics(self, successors, visited):
        #Apply MRV and LCV heuristics
        
        #Calculate MRV score (fewest onward moves)
        #Calculate LCV score (most flexibility for neighbors)
        #Sort by MRV first , then by LCV
        
        # MRV dominates, LCV helps when MRV values are equal.
        
       
        if not successors:
            return []
        
        # Calculate both scores for each successor
        scores = []
        
        for x, y in successors:
            # MRV: Count onward moves from this position
            #Counts how many legal moves are available FROM position (x, y). A lower score = more constrained = higher priority to explore first.
            mrv_score = self.count_onward_moves(x, y, visited)
            
            # LCV: Count total flexibility for neighbors
            #After visiting (x, y), it finds all next possible moves (neighbors)
            #For each neighbor, it counts how many moves that neighbor would have
            #Sums all those counts = total flexibility left after this move
            #A higher score = more flexible future = less constraining (better choice)
            temp_visited = visited | {(x, y)}
            lcv_score = 0
            
            neighbors = self.get_legal_moves(x, y, temp_visited)
            for nx, ny in neighbors:
                lcv_score += self.count_onward_moves(nx, ny, temp_visited)
            
            # Store: (mrv_score, negative lcv_score for sorting, x, y)
            # Negative LCV just to put HIGHER LCV values first
            #The negation flips the sort direction so higher LCV values come first without needing reverse=True.
            scores.append((mrv_score, -lcv_score, x, y))
        
        # Sort by MRV (ascending), then by LCV (descending via negative)
        scores.sort(key=lambda item: (item[0], item[1]))
        
        # Return sorted positions
        return [(x, y) for _, _, x, y in scores]


def successor_fct(current_x, current_y, visited, board_size=8):
    
    #Get all valid successor positions from current position
    
    #Respects all three CSP constraints:
    # Knight Move Constraint
    # All-Different Constraint
    # Board Boundaries
   
    KNIGHT_MOVES = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]
    
    successors = []
    
    for dx, dy in KNIGHT_MOVES:
        new_x = current_x + dx
        new_y = current_y + dy
        
        if 0 <= new_x < board_size and 0 <= new_y < board_size:
            if (new_x, new_y) not in visited:
                successors.append((new_x, new_y))
    
    return successors