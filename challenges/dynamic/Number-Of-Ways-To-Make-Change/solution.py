def numberOfWaysToMakeChange(n, denoms):
    total_possibilities = 0
    if 0 == n:
        return 1

    elif 0 > n:
        return 0

    for i in denoms:
        total_possibilities += numberOfWaysToMakeChange(n - i, denoms[denoms.index(i):])

    return total_possibilities