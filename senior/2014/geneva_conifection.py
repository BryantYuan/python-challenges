p = 0
t = int(input())
p += 1

for test in range(t):
    n = int(input())
    p += 1
    mountain = []
    for i in range(n):
        mountain.append(int(input()))
        p += 1

    branch = []
    mtnCar = n - 1

    nextCar = 1
    state = "Y"

    while state == "Y" and nextCar <= n:
        if mtnCar >= 0 and nextCar == mountain[mtnCar]:
            mtnCar -= 1
            nextCar += 1
        elif len(branch) > 0 and nextCar == branch[len(branch) - 1]:
            branch.pop(len(branch) - 1)
            nextCar += 1
        elif mtnCar >= 0:
            branch.append(mountain[mtnCar])
            mtnCar -= 1
        else:
            state = "N"

    print(state)
