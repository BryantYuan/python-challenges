"""Betty the cat has started going to the gym and is looking to grow her muscles.
To help with her bulk, she has bought two types of creatine-filled cookie boxes: ones
with A cookies per box, and ones with B cookies per box. Betty has an infinite
number of these. When she opens a cookie box, she is morally obligated to eat all the
cookies in the box.

Betty has a target cookie quota of K cookies a day. She wants to know: what is the
closest amount she can get to her target cookie quota, and what is the minimum number
of boxes she needs for this amount."""

cookieA, cookieB, targetAmount = tuple(input().split(' '))  # Unpacking, same as a = list[0], b =list[1]


def recursiveFunction(target, a, b):
    best_diff = float('inf')
    least_cookies = float('inf')

    if target % a == 0:
        least_cookies = target // a
        best_diff = 0
        if a > b:
            return best_diff, least_cookies
    else:
        div = target // a
        remainder = target - div * a if target - div * a > (div + 1) * a - target else (div + 1) * a - target

        if remainder == best_diff:
            if div < least_cookies:
                least_cookies = div
                best_diff = remainder

        if remainder < best_diff:
            least_cookies = div
            best_diff = remainder

    if target % b == 0:
        if target // b < least_cookies:
            least_cookies = target // b
            best_diff = 0
            if b > a:
                return best_diff, least_cookies
    else:
        div = target // b
        div += 1
        remainder = target - div * b if target - div * b > (div + 1) * b - target else (div + 1) * b - target

        if remainder == best_diff:
            if div < least_cookies:
                least_cookies = div
                best_diff = remainder

        if remainder < best_diff:
            least_cookies = div
            best_diff = remainder

    if a > b:
        starting_number = (target // a + 1) * a
        count_down = a
        other_number = b
    else:
        starting_number = (target // b + 1) * b
        count_down = b
        other_number = a

    index = 0
    for i in range(starting_number, -1, -count_down):
        new_number = i + index * other_number
        if new_number == target:
            return 0, index + i // count_down

        diff = abs(new_number - target)
        cur_cookies = index + i // count_down
        if diff < best_diff:
            best_diff = diff
            least_cookies = cur_cookies

        if diff == best_diff:
            if cur_cookies < least_cookies:
                least_cookies = cur_cookies

        index += 1

    return best_diff, least_cookies


targetAmount = int(targetAmount)
cookieA = int(cookieA)
cookieB = int(cookieB)

if cookieA > targetAmount and cookieB > targetAmount:
    print(targetAmount, 0)
else:
    result = recursiveFunction(targetAmount, cookieA, cookieB)
    print(result[0], result[1])