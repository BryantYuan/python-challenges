j = int(input())
players = int(input())

sizes = []
for i in range(j):
    sizes.append(input())

requestsSatisfied = 0
for index, size in enumerate(sizes):
    if index >= players:
        break
    pref = input().split(' ')
    number = int(pref[1]) - 1
    my_size = pref[0]
    if size != 'T':
        if my_size == 'S' or my_size == size or (my_size == 'M' and size == 'L'):
            requestsSatisfied += 1
            sizes[number] = 'T'

print(requestsSatisfied)
