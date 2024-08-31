def phoneNumberMnemonics(phoneNumber: str) -> list:
    reference = {'1': ['1'],
                 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z'],
                 '0': ['0']}
    results = []
    cur_number = phoneNumber[0]

    if len(phoneNumber) == 1:
        return reference[cur_number]

    combinations = phoneNumberMnemonics(phoneNumber[1:])
    cur_combination = reference[cur_number]

    for letter1 in cur_combination:
        for letter2 in combinations:
            results.append(letter1 + letter2)

    return results