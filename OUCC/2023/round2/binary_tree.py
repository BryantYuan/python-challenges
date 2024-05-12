class BinaryTree:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


tree = input().split(' ')
cur_level = 1
parents = []
cur_parent = None
index = 1
c_depth = 1
targets = input().split(' ')
target1 = targets[0]
target2 = targets[1]

while index <= len(tree) or (not target1 and not target2):
    c_depth += 1
    cur_nodes = tree[index:cur_level + index]
    num = 0

    for nodes in cur_nodes:
        num += 1
        new = BinaryTree(nodes, cur_parent)
        if new.value == target1:
            node1 = new
            depth1 = c_depth
            target1 = True
        elif new.value == target2:
            node2 = new
            depth2 = c_depth
            target2 = True

        parents.append(new)
        if num == 2:
            num = 0
            del parents[0]
            if parents:
                cur_parent = parents[0]

    index += cur_level
    cur_level *= 2

expected_depth = min(depth1, depth2)

if depth1 != expected_depth:
    depth = depth1
    while depth > expected_depth:
        node1 = node1.parent
        depth -= 1

elif depth2 != expected_depth:
    node = node2
    depth = depth2
    while depth > expected_depth:
        node2 = node2.parent
        depth -= 1

while node1.parent != node2.parent:
    node1 = node1.parent
    node2 = node2.parent

print(node1.parent.value)
