from Puzzle import puzzle
from queue import PriorityQueue , Queue , LifoQueue
 

# Breadth-first Search:
def BFS(given_state):
    root = puzzle(given_state, None, None, 0, 0)
    if root.check_goal():
        return root.solver()
    frontier = Queue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        explored.append(current_node.state) 
        children = current_node.expand_graph()
        for child in children:
            if child.state not in explored:
                if child.check_goal():
                    return child.solver(), len(explored)
                frontier.put(child)
    return


# Depth-first Search with limited depth:
def DFS(given_state): 
    root = puzzle(given_state, None, None, 0, 0)
    if root.check_goal():
        return root.solver()
    frontier = LifoQueue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        max_depth = current_node.depth #current depth
        explored.append(current_node.state)
        
        if max_depth >= 15: # I do not recommend to make this unlimited,
                            # it will take forever to find a solution .
            continue # Goes to the next branch, from top .

        children = current_node.expand_graph()
        for child in children:
            if child.state not in explored:
                if child.check_goal():
                    return child.solver(), len(explored)
                frontier.put(child)
    return (("Couldn't solve the puzzle in the {} depth.".format(max_depth)), len(explored))
        

# Greedy algorithm that expands every lefty node first .
def greedy(given_state):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = puzzle(given_state, None, None, 0, 0)
    #root.evaluation()
    evaluation = root.heuristic_manhattan_distance() # We can use heuritic_misplaced_counter() instead.
    frontier.put((evaluation[0], counter, root)) # Based on greedy evaluation.

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.check_goal():
            return current_node.solver(), len(explored)

        children = current_node.expand_graph()
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.heuristic_manhattan_distance() #we can use heuritic_misplaced_counter() instead.
                frontier.put((evaluation[0], counter, child)) #based on Greedy_eval_func
    return


# A* algorithm 
def Astar(given_state):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    n = 3
    root = puzzle(given_state, None, None, 0, 0)
    evaluation = root.heuristic_manhattan_distance() #we can use heuritic_misplaced_counter() instead.
    frontier.put((evaluation[1], counter, root)) #based on Astar_eval_func

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.check_goal():
            return current_node.solver(), len(explored)

        children = current_node.expand_graph()
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.heuristic_manhattan_distance() #we can use heuritic_misplaced_counter() instead.
                frontier.put((evaluation[1], counter, child)) # Based on Astar_eval_func
    return


# Same DFS algorithm, with user defined depth 
def IDS(given_state,depth): 
    root = puzzle(given_state, None, None, 0, 0)
    if root.check_goal():
        return root.solver()
    frontier = LifoQueue()
    frontier.put(root)
    explored = []

    while not(frontier.empty()):
            current_node = frontier.get()
            max_depth = current_node.depth
            explored.append(current_node.state)
            
            if max_depth == depth:
                continue # Goes to next node to expand .

            children = current_node.expand_graph()
            for child in children:
                if child.state not in explored:
                    if child.check_goal():
                        return child.solver(), len(explored)
                    frontier.put(child)
                
           
    return (("Couldn't solve the puzzle in the limited depth."), len(explored))