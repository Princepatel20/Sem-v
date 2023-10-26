import heapq
def dijkstra(graph, start):
 shortest_distance = {node: float('inf') for node in graph}
 shortest_distance[start] = 0
 priority_queue = [(0, start)]
 while priority_queue:
 current_distance, current_node = heapq.heappop(priority_queue)
 if current_distance > shortest_distance[current_node]:
 continue
 for neighbor, weight in graph[current_node].items():
 distance = current_distance + weight
 if distance < shortest_distance[neighbor]:
 shortest_distance[neighbor] = distance
 heapq.heappush(priority_queue, (distance, neighbor))
return shortest_distance
graph = {
 'A': {'B': 1, 'C': 4},
 'B': {'A': 1, 'C': 2, 'D': 5},
 'C': {'A': 4, 'B': 2, 'D': 1},
 'D': {'B': 5, 'C': 1},
 'E': {'A': 6, 'B': 7},
 'F': {'C': 7, 'D': 2}
}
start_node = 'A'
result = dijkstra(graph, start_node)
for node, distance in result.items():
 print(f'Shortest distance from {start_node} to {node}: {distance}')
