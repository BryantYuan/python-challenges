total_numbers = int(input())
numbers = []
total_sum = 0
for i in range(total_numbers):
    next_num = int(input())
    if next_num == 0:
        try:
            total_sum -= numbers.pop()
        except IndexError:
            continue
    else:
        numbers.append(next_num)
        total_sum += next_num
print(total_sum)
