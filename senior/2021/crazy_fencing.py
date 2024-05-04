total_fences = int(input())
fence_lens = input().split(' ')
fence_bottoms = input().split(' ')
index1 = 0
index2 = 1
total = 0
bottoms = 0
while index2 < len(fence_lens):
    side1 = int(fence_lens[index1])
    side2 = int(fence_lens[index2])
    bottom = int(fence_bottoms[bottoms])
    area = (side1 + side2) * bottom / 2
    total += area
    index1 += 1
    index2 += 1
    bottoms += 1
    
print(total)
