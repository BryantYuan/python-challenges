steps_available: int = int(input())
steps_remaining: dict = {}


def climb(_cur_steps_left):
    total = 0
    if 0 == _cur_steps_left:
        return 1

    elif 0 > _cur_steps_left:
        return 0

    if _cur_steps_left not in steps_remaining:

        for i in range(1, 3):
            total += climb(_cur_steps_left - i)
        steps_remaining[_cur_steps_left] = total

    else:
        return steps_remaining[_cur_steps_left]

    return total


print(climb(steps_available))