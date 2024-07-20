def majorityElement(array: list) -> int:
    half = len(array) // 2
    number_tracker = {}

    if half == 0:
        return array[0]

    for num in array:
        if num in number_tracker:
            number_tracker[num] += 1
            if number_tracker[num] > half:
                return num
            continue

        number_tracker[num] = 1

    return -1