total = int(input())
if total == 1:
    print(input())
else:
    scrambled = input().split(' ')
    sorted_list = []
    for s in scrambled:
        sorted_list.append(int(s))

    sorted_list.sort()
    stop = total // 2
    if stop * 2 != total:
        stop += 1
    low = sorted_list[:stop]
    high = sorted_list[stop:]
    high.reverse()
    correct = ''

    while low or high:
        if len(low) != 0:
            correct += str(low[-1]) + ' '
            del low[-1]
        if len(high) != 0:
            correct += str(high[-1]) + ' '
            del high[-1]

    print(correct)
