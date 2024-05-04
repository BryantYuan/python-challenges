ports = int(input())
numPlanes = int(input())

planes = []

total = 0

for i in range(ports + 1):
    planes.append(0)

i = 0
keepGoing = True
while i < numPlanes and keepGoing:
    cPlane = int(input())
    while cPlane > 0 and planes[cPlane] > 0:
        t = planes[cPlane]
        planes[cPlane] += 1
        cPlane -= t
    if cPlane <= 0:
        keepGoing = False
    else:
        planes[cPlane] = 1
        total += 1
    i += 1

print(total)
