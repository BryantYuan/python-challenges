"""Betty the cat has started going to the gym and is looking to grow her muscles.
To help with her bulk, she has bought two types of creatine-filled cookie boxes: ones
with A cookies per box, and ones with B cookies per box. Betty has an infinite
number of these. When she opens a cookie box, she is morally obligated to eat all the
cookies in the box.

Betty has a target cookie quota of K cookies a day. She wants to know: what is the
closest amount she can get to her target cookie quota, and what is the minimum number
of boxes she needs for this amount."""

cookieA, cookieB, targetAmount = tuple(input().split(' '))  # Unpacking, same as a = list[0], b =list[1]


def findTarget(target, a, b):
    boxes_needed = round(target / a)
    diff = abs(boxes_needed * a - target)

    if diff == 0 and a >= b:
        return 0, boxes_needed

    least_cookies = boxes_needed
    best_diff = diff

    # Time to check B

    boxes_needed = round(target / b)
    diff = abs(boxes_needed * b - target)

    if diff == 0:
        return 0, boxes_needed

    if diff < best_diff:
        best_diff = diff
        least_cookies = boxes_needed
    elif diff == best_diff:
        if boxes_needed < least_cookies:
            best_diff = diff
            least_cookies = boxes_needed

    larger_number = a if a > b else b
    smaller_number = a if a < b else b
    starting_number = target // larger_number * larger_number

    for number in range(starting_number, 0, -larger_number):
        if (target - number) % smaller_number == 0:
            boxes_needed = number // larger_number + (target - number) // smaller_number
            return 0, boxes_needed

        if best_diff == 0:
            continue

        div = round((target - number) / smaller_number)
        diff = abs(target - (div * smaller_number + number))
        boxes_needed = div + number // larger_number

        if diff < best_diff:
            best_diff = diff
            least_cookies = boxes_needed
        elif diff == best_diff:
            if boxes_needed < least_cookies:
                best_diff = diff
                least_cookies = boxes_needed

    return best_diff, least_cookies


targetAmount = int(targetAmount)
cookieA = int(cookieA)
cookieB = int(cookieB)

if cookieA > targetAmount and cookieB > targetAmount:
    print(targetAmount, 0)
else:
    result = findTarget(targetAmount, cookieA, cookieB)
    print(result[0], result[1])