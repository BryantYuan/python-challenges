r_l = input().split()
rows = int(r_l[0])
length = int(r_l[1])


for i in range(rows):
    string = input()
    amount = {}
    heavy_or_light = {}

    for s in string:
        try:
            amount[s] += 1
            heavy_or_light[s] = 'h'
        except KeyError:
            amount[s] = 1
            heavy_or_light[s] = 'l'

    if heavy_or_light[string[0]] == 'h':
        nex = 'h'
    else:
        nex = 'l'

    false = False

    for index in range(0, len(string)):
        s1 = string[index]

        if heavy_or_light[s1] == nex:
            if nex == 'l':
                nex = 'h'
            else:
                nex = 'l'
            pass
        else:
            false = True
            break

    if not false:
        print('T')
    else:
        print('F')
