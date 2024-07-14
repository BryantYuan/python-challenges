def fourNumberSum(array, targetSum, cache=None, cur_sum=0, number_of_items=0):
    list_of_sums = []

    if cache is None:
        cache = {}

    for index, num in enumerate(array):
        if number_of_items == 1:
            if cur_sum + num in cache:
                cache[cur_sum + num].append([num, cur_sum])
            else:
                cache[cur_sum + num] = [[num, cur_sum]]

            if targetSum - cur_sum - num in cache:
                new = [num]
                for item in cache[targetSum - cur_sum - num]:
                    if item in array:
                        new.extend(item)
                        list_of_sums.append(new)

        if number_of_items + 1 == 4:
            if cur_sum + num == targetSum:
                return [[num]]
            return []

        result = fourNumberSum(array[index + 1:], targetSum, cache, cur_sum + num, number_of_items + 1)
        if len(result) > 0:
            new = [num]
            for n in result:
                new.extend(n)
                list_of_sums.append(new)
                new = [num]

    return list_of_sums