def fourNumberSum(array, targetSum):
    if len(array) < 4:
        return []

    cache = {array[0] + array[1]: [[array[0], array[1]]]}
    result = []

    for index in range(2, len(array) - 1):
        cur_val = array[index]

        for num in array[index + 1:]:
            cur_total = num + cur_val
            cur_gap = targetSum - cur_total
            if cur_gap not in cache:
                continue

            for existing_pair in cache[cur_gap]:
                result.append(existing_pair + [cur_val, num])

        for prev_num in array[:index]:
            cur_total = cur_val + prev_num
            cache.setdefault(cur_total, []).append([prev_num, cur_val])

    return result
