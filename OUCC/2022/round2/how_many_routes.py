class Node:
    def __init__(self, value, ):
        self.value = value
        self.next_node = []
        self.previous_node = None
        self.routes = 0


nodes = input().split(',')
all_nodes = {}
for i in nodes:
    all_nodes[i] = Node(i)

total = int(input())
for i in range(total):
    new = input().split(',')
    all_nodes[new[0]].next_node.append(all_nodes[new[1]])
    all_nodes[new[1]].previous_node = all_nodes[new[0]]


def find_route(end, start):
    total_pos = 0
    if start == end:
        return 1

    if start.routes != 0:
        return start.routes

    pos = start.next_node
    for p in pos:
        cur_possibilities = find_route(end, p)
        total_pos += cur_possibilities
        p.routes = cur_possibilities

    return total_pos


print(find_route(all_nodes[nodes[-1]], all_nodes[nodes[0]]))
