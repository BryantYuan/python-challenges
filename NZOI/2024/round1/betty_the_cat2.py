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
    larger_number = max(a, b)
    smaller_number = min(a, b)

    if target % larger_number == 0:
        return 0, target // larger_number

    number_of_cookies_used = round(target / larger_number)
    best_diff = abs(target - number_of_cookies_used * larger_number)
    least_cookies = number_of_cookies_used

    cur_number = number_of_cookies_used * larger_number                           
    while cur_number >= 0:
        gap = abs(target - cur_number)
        cur_diff = abs(target - (round(gap / smaller_number) * smaller_number + cur_number))
        cur_cookies = round(gap / smaller_number) + number_of_cookies_used

        if cur_diff == 0:
            return 0, cur_cookies

        if cur_diff < best_diff:
            best_diff = cur_diff
            least_cookies = cur_cookies

        elif cur_diff == best_diff:
            if cur_cookies < least_cookies:
                best_diff = cur_diff
                least_cookies = cur_cookies

        number_of_cookies_used -= 1
        cur_number = number_of_cookies_used * larger_number

    return best_diff, least_cookies


targetAmount = int(targetAmount)
cookieA = int(cookieA)
cookieB = int(cookieB)

if cookieA > targetAmount and cookieB > targetAmount:
    print(targetAmount, 0)
else:
    result = findTarget(targetAmount, cookieA, cookieB)
    print(result[0], result[1])