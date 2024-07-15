def fourNumberSum(array, targetSum):
    result = doFourNumberSum(array, targetSum, {}, 0)
    return result


def doFourNumberSum(array, targetSum, cache, number_of_items) -> list:
    list_of_sums = []

    number_of_items += 2
    for index in range(len(array) - 1):
        value1 = array[index]
        for index2 in range(index + 1, len(array)):
            value2 = array[index2]
            if number_of_items == 4:
                if value1 + value2 == targetSum:
                    list_of_sums.append([value1, value2])
                continue

            result = doFourNumberSum(array[index2 + 1:], targetSum - value1 - value2, cache, number_of_items)
            if len(result) > 0:
                for i in range(len(result)):
                    new = [value1, value2, result[i][0], result[i][1]]
                    list_of_sums.append(new)

    return list_of_sums


def getPairs(array, cache):
    cur_num = array[-1]
    for num in array[:-1]:
        if cur_num + num in cache:
            cache[cur_num + num].append([cur_num, num])
        else:
            cache[cur_num + num] = [cur_num, num]
    return cache