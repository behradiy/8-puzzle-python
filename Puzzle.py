class puzzle:
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0] # You might want ot change this to any 
                                             # other desired states .  
    
    # becasue A* and greedy algorithm, use diffrent heuristics.
    Greedy_eval_func = None
    Astar_eval_func = None
    heuristic_func = None
    
    def __init__(self, state, parent, move, depth, cost): # defining the graphs and ... 
        self.move = move
        self.depth = depth
        self.state = state
        self.parent = parent
        if parent: self.cost = parent.cost + cost
        else: self.cost = cost

    #heuristic_func using misplaced tiles:
    def heuritic_misplaced_counter(self): 
        counter = 0
        n = 3
        self.heuristic_func = 0 # making sure there's no old buffered value .
        for i in range(n*n):
            for j in range(n*n):
                if (self.state[j] != self.goal_state[i]):
                    counter += 1 # Counting the misplaced tiles . 
                self.heuristic_func = self.heuristic_func + counter

        self.Greedy_eval_func = self.heuristic_func   #Handling the greedy heuristic
        self.Astar_eval_func = self.heuristic_func + self.cost #handling the Astar heuristic

        return( self.Greedy_eval_func, self.Astar_eval_func)  

    #heuristic_func using manhattan distance:
    def heuristic_manhattan_distance(self): 
        self.heuristic_func = 0
        n = 3
        for i in range(1 , n*n):
            distance = abs(self.state.index(i) - self.goal_state.index(i)) # Calculating the manhattan distance .
            self.heuristic_func = self.heuristic_func + distance/n + distance%n 

        self.Greedy_eval_func = self.heuristic_func    
        self.Astar_eval_func = self.heuristic_func + self.cost
        
        return( self.Greedy_eval_func, self.Astar_eval_func)
    
    # Returns the given state's move + it's parent's move untill all parents are visited .
    def solver(self):
        path = self
        solver = []
        solver.append(self.move)
        
        while path.parent != None:
            path = path.parent
            solver.append(path.move)
            
        solver = solver[:-1]
        solver.reverse()
        return solver
                  
    @staticmethod
    # Checks the state to validate which moves are possible:
    def possible_moves(x): 
        moves = ['Left', 'Right', 'Up', 'Down']
        
        if (x % 3) == 0:
            moves.remove('Left')

        if (x % 3) == 2:
            moves.remove('Right')

        if (x - 3 )< 0:
            moves.remove('Up')

        if (x + 3) > 8:
            moves.remove('Down')

        return moves
    
    # If the number of inversions is EVEN then puzzle would be solvable .     
    def if_solvable(state):
        counter = 0
        for i in range(len(state)-1):
            for j in range(i+1 , len(state)):
                if (( state[i] > state[j]) and state[i] and state[j]):
                    counter += 1 # Counting Inversions 
    
        if counter %2 == 0 :
            print("Puzzle is solvable, please wait. \n")
            return True
        print("puzzle is not solvable! try a diffrent initial state")
        return False 
    
    # Compares the given state and goal state:
    def check_goal(self):
        if self.state == self.goal_state: return True
        else: return False

    # Expands nodes with given state .
    def expand_graph(self): 
        i = self.state.index(0)
        all_moves = self.possible_moves(i)
        children_added = []
        
        for move in all_moves:
            copied_state = self.state.copy()
            if move=='Up':
                copied_state[i], copied_state[i-3]= copied_state[i-3], copied_state[i]

            elif move=='Down':
                copied_state[i], copied_state[i+3]= copied_state[i+3], copied_state[i]

            elif move=='Left':
                copied_state[i], copied_state[i-1]= copied_state[i-1], copied_state[i]

            else: # It has to be "Right" .
                copied_state[i], copied_state[i+1]= copied_state[i+1], copied_state[i]
                
            children_added.append(puzzle(copied_state, self, move, self.depth + 1, 1)) # Depth should be changed as children_added is being produced .
        
        return children_added
