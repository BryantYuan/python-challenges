number_of_days = int(input())
aardvarkAsylum = list(map(int, input().split()))
basiliskBiosphere = list(map(int, input().split()))
difference_counts = dict()

for day_a in aardvarkAsylum:
    for day_b in basiliskBiosphere:
        key = day_b - day_a

        if key not in difference_counts.keys():
            difference_counts[key] = 1
            continue

        difference_counts[key] += 1

print(2 * number_of_days - max(difference_counts.values()))