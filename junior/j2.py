size = int(input())
next_y = int(input())
while size > next_y:
    size += next_y
    next_y = int(input())

print(size)
