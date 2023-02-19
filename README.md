# 8-Puzzle solution using python and different search algorithms

## About search algorithms 

Search algorithms work to retrieve information stored within particular data structure, or calculated in the search space of a problem domain, with either discrete or continuous values.

Although search engines use search algorithms, they belong to the study of information retrieval, not algorithmics. keep in mind that we're using the graph data structure in this code. 

Algorithms used in this code are : 
1. A* search
2. BFS 
3. DFS
4. IDS
5. Greedy search  
----
## **Breif explanation on algorithms**
### **A*** search :
Like Dijkstra, A* works by making a **lowest-cost path tree** from the start node to the target node. What makes A* different and better for many searches is that for each node, A* uses a function 
f(n) that gives an estimate of the total cost of a path using that node. Therefore, A* is a heuristic function, which differs from an algorithm in that a heuristic is more of an estimate and is not necessarily provably correct.

A* expands paths that are already less expensive by using this function:

>f(n) = g(n) + h(n)

where
- f(n) = total estimated cost of path through node 
- g(n) = cost so far to reach node 
- h(n) = estimated cost from n to goal.
- This is the heuristic part of the cost function, so it is like a guess.

----
 
### **BFS** search :

The algorithm efficiently visits and marks all the key nodes in a graph in an accurate breadthwise fashion. This algorithm selects a single node (initial or source point) in a graph and then visits all the nodes adjacent to the selected node. Remember, BFS accesses these nodes one by one.

Once the algorithm visits and marks the starting node, then it moves towards the nearest unvisited nodes and analyses them. Once visited, all nodes are marked. These iterations continue until all the nodes of the graph have been successfully visited and marked.

----
### **DFS** search :

The algorithm starts at the root (top) node of a tree and goes as far as it can down a given branch (path), then backtracks until it finds an unexplored path, and then explores it. The algorithm does this until the entire graph has been explored.

Depth-first searches are often used as subroutines in other more complex algorithms. For example, the [matching algorithm](https://brilliant.org/wiki/matching-algorithms/), [Hopcroft–Karp](https://brilliant.org/wiki/hopcroft-karp/), uses a DFS as part of its algorithm to help to find a matching in a graph.


----
### **IDS** search :
IDS (iterative deepening search) is exaclty like normal DFS but the only vary is that the detph of search is limited and whenever the algorithm reaches the defined depth, it would start searching another branch (parent) from top. this algorithm is optimal only if there is a solution in that limited depth. otherwise the algorithm would fail in case of finding a solution. 

----
### **Greedy** search :

The algorithm makes the optimal choice at each step as it attempts to find the overall optimal way to solve the entire problem. Greedy algorithms are quite successful in some problems, such as [Huffman encoding](https://brilliant.org/wiki/huffman-encoding/) which is used to compress data, or Dijkstra's algorithm, which is used to find the shortest path through a graph.
However, in many problems, a greedy strategy does not produce an optimal solution. Greedy algorithm wouldn't find optimal sulotion in most of the problems but at each step it is choosing optimal options.


---

## Code's explanation

this repo contains three files : 
- Algos.py: This file contains all the described algorithms as functions. 
- Puzzle.py: the puzzle class which defines the graph data structure we talked about. 
- Driver.py: you need to run this file to make everything happen.

there's no requirements.txt 