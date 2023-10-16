# Define graph as adjacency list 
 graph = { 
   'a': ['b', 'c'], 
   'b': ['d', 'e'], 
   'c': ['f'], 
   'd': [], 
   'e': ['f'], 
   'f': [] 
 } 
  
 # Function for breadth-first search 
 def bfs(graph, start, end): 
   visited = [] 
   queue = [start] 
  
   while queue: 
     current = queue.pop(0)  
     if current not in visited: 
       visited.append(current) 
       if current == end: 
         print(visited) 
         return 
       neighbors = graph[current] 
       for neighbor in neighbors: 
         queue.append(neighbor) 
  
 # Call BFS function   
 bfs(graph, 'a', 'f')
