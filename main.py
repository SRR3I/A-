def a_star(graph, start, goal):
    open_list = [(start, 0, graph[start][0], [])]
    print(open_list)
    closed_set = set()

    while open_list:
        current_node, g_cost, heuristic, path = min(
            open_list, key=lambda x: x[1] + x[2])

        if current_node == goal:
            return path + [current_node]

        open_list.remove((current_node, g_cost, heuristic, path))
        closed_set.add(current_node)

        for neighbor, cost in graph[current_node][1].items():
            if neighbor in closed_set:
                continue
            g_cost_neighbor = g_cost + cost
            heuristic_neighbor = graph[neighbor][0]
            new_path = path + [current_node]
            open_list.append((neighbor, g_cost_neighbor,
                             heuristic_neighbor, new_path))

    return None


# Given graph
graph = {
    'A': [40, {'B': 8, 'C': 5, 'D': 27}],
    'B': [20, {'E': 15, 'F': 18}],
    'C': [25, {'G': 7, 'H': 28, 'I': 12}],
    'D': [27, {'I': 7}],
    'E': [50, {}],
    'F': [60, {}],
    'G': [18, {'H': 15}],
    'H': [10, {'J': 7, 'K': 4}],
    'I': [18, {'H': 18}],
    'J': [12, {}],
    'K': [0, {}]
}

# Example usage
start_node = 'A'
goal_node = 'K'
path = a_star(graph, start_node, goal_node)
print("Path from", start_node, "to", goal_node, ":", path)
