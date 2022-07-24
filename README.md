# Graphs
Important Problems on Graphs

TIPS - 

Number of connected components - DFS and return count


To check cyclic in Undirected Graph - Check connected components. if Total edges == Total nodes - connected components then not cyclic

Cyclic in Directed Graph - Topological sort. Count nodes intserted to answer array. IF Count != A: Cycle is formed.

Undirected graph - Shortest path form source to destination - BFS

Directed graph - Shortest path form source to destination - Dijkstra

=========================

Topological sort - 
1.Create Adjacency List 
2.Create Indegree List - Number of incoming edges to nodes.
3.Put Indegree with 0 in queue.
4. While q, 
          popleft,
          append to ans, 
          iterate over adjacency list,
          decrement indegree,
          if indegree is 0, put in q.
5. Return Answer

Note - IF there is a cycle you cannot get topological sort.
