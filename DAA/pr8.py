from collections import defaultdict

def topological_sort(graph):
    visited = set()
    stack = []

    def visit(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                visit(neighbor)
            stack.append(node)

    for node in list(graph):
        visit(node)

    return stack[::-1]

graph = defaultdict(list)
graph["heat griddle"].append("mix ingredients")
graph["mix ingredients"].append("spoon mix onto griddle")
graph["mix ingredients"].append("heat up syrup")
graph["spoon mix onto griddle"].append("flip pancakes")
graph["flip pancakes"].append("cook until golden brown on the bottom")

order_of_steps = topological_sort(graph)
for step in order_of_steps:
    print(step)
