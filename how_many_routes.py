class Node:
    pass


all_nodes = input().split(',')
total = int(input())
paths = {}
for i in range(total):
    new = input().split(',')
    try:
        paths[new[0]].append(new[1])
    except KeyError:
        paths[new[0]] = [new[1]]

    try:
        paths[new[1]].append(new[0])
    except KeyError:
        paths[new[1]] = [new[0]]


def find_route(connections, end, start, prev):
    total_pos = 0
    if start == end:
        return 1
    prev.append(start)
    pos = connections[start]
    for p in pos:
        if p not in prev:
            total_pos += find_route(connections, end, p, prev)
    prev.remove(start)

    return total_pos


print(find_route(paths, all_nodes[-1], all_nodes[0], []))
