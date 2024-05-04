r: int = int(input())
c: int = int(input())
matrix: list = [['' for j in range(c)] for i in range(r)]
graphMap: dict = {}

for i in range(r):
    lineInfo: list = input().split(" ")
    for j in range(len(lineInfo)):
        val: int = int(lineInfo[j])
        matrix[i][j] = val
        lists: list = graphMap[val] if val in graphMap.keys() else []
        lists.append([i + 1, j + 1])
        graphMap[val] = lists


def doCheckCanEscape(row: int, col: int, graph: list, locations: dict) -> bool:
    if row < 0 or col < 0 or row > len(graph) or col > len(graph[0]):
        return False

    if row == 1 or col == 1:
        return True

    val: int = row * col

    try:
        outputs: list = locations[val]
    except KeyError:
        return False

    if len(outputs) != 0:
        for output in outputs:
            found: bool = doCheckCanEscape(output[0], output[1], graph, locations)
            if found:
                return True

    return False


if doCheckCanEscape(len(matrix), len(matrix[0]), matrix, graphMap):
    print('yes')
else:
    print('no')
