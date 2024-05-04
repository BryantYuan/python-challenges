total = int(input())
diff = total // 2
same = 0
hats = []
for i in range(total):
    hats.append(input())

for i in range(total // 2):
    if hats[i] == hats[diff + i]:
        same += 2

print(same)
