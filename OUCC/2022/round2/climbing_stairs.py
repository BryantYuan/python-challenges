steps_available = int(input())


def climb(_cur_steps_left):
    total = 0
    if 0 == _cur_steps_left:
        return 1
    elif 0 > _cur_steps_left:
        return 0
    for i in range(1, 3):
        total += climb(_cur_steps_left - i)

    return total


print(climb(steps_available))
