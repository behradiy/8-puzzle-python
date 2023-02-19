from Puzzle import puzzle
from Algos import BFS, DFS, greedy, Astar, IDS
import time 

#Initial state
root_state = [1,2,3,4,5,6,0,7,8] # Any pull request in order to making this,
                                 # randomly generated would be appreciated a lot .

print("The initial state is:", root_state)
print("The goal state is:", puzzle.goal_state,"\n")

if puzzle.if_solvable(root_state): # i mean, Come On . 
    
    print("BFS algorithm running:")
    tik1 = time.time()
    BFS_solution = BFS(root_state)
    tok1 = time.time() - tik1
    print('BFS solution:', BFS_solution[0])
    print('Time it took:', round(tok1,4),"sec")
    print('Nodes expanded:', BFS_solution[1])    
    
    print("\n","DFS algorithm running:")
    tik2 = time.time()
    DFS_solution = DFS(root_state) # It's limited on 15 .
    tok2 = time.time() - tik2
    print('DFS solution:', DFS_solution[0])
    print('Time it took:', round(tok2,4),"sec")  
    print('Nodes expanded:', DFS_solution[1])
    
    print("\n","greedy algorithm running:")
    tik3 = time.time()
    greedy_solution = greedy(root_state)
    tok3 = (time.time()) - tik3
    print('Greedy solution:', greedy_solution[0])
    print('Time it took:', round(tok3,4),"sec")
    print('Nodes expanded:', greedy_solution[1])   
    
    print("\n","A* algorithm running:")
    tik4 = time.time()
    Astar_solution = Astar(root_state)
    tok4 = time.time() - tik4
    print('A* solution:', Astar_solution[0])
    print('Time it took:', round(tok4,4),"sec")
    print('Nodes expanded:', Astar_solution[1])  
    
    print("\n","IDS algorithm running:")
    tik6 = time.time()
    IDS_solution = IDS(root_state, 30) # we give it a depth
    tok6 = time.time() - tik6
    print('IDS solution:', IDS_solution[0])
    print('Time it took:', round(tok6,4),"sec")
    print('Nodes expanded:', IDS_solution[1])

else:
    print("this isn't solavable, try changing the root state.")