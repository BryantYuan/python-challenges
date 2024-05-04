participants = int(input())
scores = {}
gold = -1
silver = -1
bronze = -1
for i in range(participants):
    score = int(input())
    try:
        scores[score] += 1
    except KeyError:
        scores[score] = 1
        if score > gold:
            bronze = silver
            silver = gold
            gold = score
        elif score > silver:
            bronze = silver
            silver = score
        elif score > bronze:
            bronze = score


print(bronze, scores[bronze])
