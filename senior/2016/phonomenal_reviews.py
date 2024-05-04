places = input().split(' ')
eating_places = int(places[0])
total_places_to_go = places[1]
places_to_go = input().split(' ')
status = {}
roads = {}

for i in range(eating_places - 1):
    connection = input().split(' ')
    road1 = connection[0]
    road2 = connection[1]
    try:
        roads[road1].append(road2)
    except KeyError:
        roads[road1] = [road2]
        if road1 in places_to_go:
            status[road1] = True
        else:
            status[road1] = False
    try:
        roads[road2].append(road1)
    except KeyError:
        roads[road2] = [road1]
        if road2 in places_to_go:
            status[road2] = True
        else:
            status[road2] = False


def visiting(cur_position, paths, statuses, prev, visited):
    best = float('inf')
    current_paths = 0
    possible_places = paths[cur_position]
    for place in possible_places:
        cur_status = statuses[place]
        if place != prev:
            if cur_status:
                current_paths += 1
                current_paths += visiting(place, paths, statuses, cur_position, visited)
                if current_paths < best:
                    best = current_paths
            elif len(paths[place]) > 1:
                current_paths += 1
                current_paths += visiting(place, paths, statuses, prev, visited)
                if current_paths < best:
                    best = current_paths
            else:
                continue

    return best


least = float('inf')
for pho in places_to_go:
    cur = visiting(pho, roads, status, pho, [])
    if cur < least:
        least = cur

print(least)
