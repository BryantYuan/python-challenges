def longestSubstringWithoutDuplication(string):
    duplicates = {}  # Key is char, Value is index.
    best = ''
    best_length = 0
    cur_substring = ''
    cur_length = 0

    index = 0
    while index < len(string):
        char = string[index]
        if char in duplicates:
            index = duplicates[char]
            if cur_length > best_length:
                best = cur_substring
                best_length = cur_length

            cur_substring = ''
            duplicates = {}
            cur_length = 0

        else:
            cur_length += 1
            cur_substring = cur_substring + char
            duplicates[char] = index

        index += 1

    if cur_length > best_length:
        best = cur_substring
    return best