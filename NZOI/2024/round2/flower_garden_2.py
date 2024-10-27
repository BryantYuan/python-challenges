times, distance = map(int, input().split(' '))
total_width = distance * 2 + 1
list_of_areas = []
longest_height = -1
longest_width = -1
total = 0

for i in range(times):
    center = input().split(' ')
    x = int(center[0])
    y = int(center[1])

    if y + distance > longest_height:
        for j in range(y - longest_height + distance):
            list_of_areas.append(['0'] * (longest_width + 1))
        longest_height = y + distance

    if x + distance > longest_width:
        for j in range(longest_height + 1):
            list_of_areas[j].extend(['0'] * (x - longest_width + 1 + distance))
        longest_width = x + distance

    h_start = y - distance
    h_end = y + distance
    w_start = x - distance
    w_end = x + distance

    for height in range(h_start, h_end + 1):
        if height < 0:
            continue

        for width in range(w_start, w_end + 1):
            if width < 0:
                continue

            node = list_of_areas[height][width]
            if node == '0':
                list_of_areas[height][width] = '1'
                total += 1

print(total)