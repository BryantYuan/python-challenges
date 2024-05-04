n = int(input())
boards = []
prev = ''
for i in input(''):
    if i == ' ':
        boards.append(int(prev))
        prev = ''
    else:
        prev += i
boards.append(int(prev))


def search(total, board):
    total_count = 0
    for index, b in enumerate(board):
        if total - b == 0:
            return True, 1
        else:
            if index + 1 < len(board) and b < total:
                r = search(total - b, board[index + 1:])
                if r[0]:
                    return True, 1
                total_count += r[1]

    if total_count > 0:
        return True, total_count
    return False, 0


best = 0
t = sum(boards)
if n == 1:
    print(1, 1)
elif t % 2 != 0:
    print(1, sum([i for i in range(1, n)]))
else:
    target = t // (n // 2)
    rc = search(target, boards)
    print(t // target, rc[1])