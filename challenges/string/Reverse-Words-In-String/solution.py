def reverseWordsInString(string: str) -> str:
    result = ''
    cur_word = ''
    for char in string:
        if char != ' ':
            cur_word += char
            continue

        result = ' ' + cur_word + result
        cur_word = ''

    result = cur_word + result

    return result
