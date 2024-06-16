def cycleInGraph(edges: list) -> bool:
    visited = {}
    map_of_nodes = {}
    for index, edge in enumerate(edges):
        map_of_nodes[index] = edge
        visited[index] = False

    for i in range(len(edges)):
        result = doCycleInGraph(visited, map_of_nodes, i)
        if result:
            return True
    return False


def doCycleInGraph(visited, map_of_nodes, cur_node) -> bool:
    if visited[cur_node]:
        return True

    visited[cur_node] = True
    next_nodes = map_of_nodes.get(cur_node)
    for next_node in next_nodes:
        result = doCycleInGraph(visited, map_of_nodes, next_node)
        if result:
            return True

    visited[cur_node] = False
    return False