def findMultiples(num):
    total_comb = 0
    max_a = num // 4
    for i in range(max_a + 1):
        fours = 4 * i
        remainder = num - fours
        if remainder % 5 == 0:
            total_comb += 1
    return total_comb


print(findMultiples(int(input())))