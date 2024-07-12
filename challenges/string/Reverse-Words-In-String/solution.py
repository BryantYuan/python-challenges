def reverseWordsInString(string: str) -> str:
    result = ''
    cur_word = ''
    for char in string:
        if char != ' ':
            cur_word += char
            continue

        new = ' ' + cur_word + result
        result = new
        cur_word = ''

    new = cur_word + result
    result = new

    return result