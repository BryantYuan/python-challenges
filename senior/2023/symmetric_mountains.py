def findAsymmetricValue(total, length):
    index1 = 0
    index2 = length
    best = float('inf')

    while index2 < len(total):
        cur = total[index1:index2]
        i = 0
        j = length - 1
        asymmetricValue = 0

        while i < j:
            num1 = int(cur[i])
            num2 = int(cur[j])
            value = abs(num1 - num2)
            asymmetricValue += value
            i += 1
            j -= 1

        if asymmetricValue < best:
            best = asymmetricValue
        index1 += 1
        index2 += 1
    return best


t_mountains = int(input())
mountains = input().replace(' ', '')
total = ''
for i in range(1, t_mountains):
    value = findAsymmetricValue(mountains, i)
    total += str(value) + ' '

print(total)
