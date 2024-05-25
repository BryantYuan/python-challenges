grid = {(i,j):False for i in range(1,6) for j in range(1,6)}
commands = [(int(x[0]),x[1]) for x in input().split(' ')]

for command in commands:
  if command[1] == 'R':
    lamps = [(command[0],j) for j in range(1,6)]
  else:
    lamps = [(i,command[0]) for i in range(1,6)]
  for lamp in lamps:
    grid[lamp] = not grid[lamp]

for i in range(1,6):
  print(''.join(str(int(grid[(i,j)])) for j in range(1,6)))
# 3R 5C 2R 1C