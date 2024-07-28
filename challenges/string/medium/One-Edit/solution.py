def oneEdit(stringOne, stringTwo):
    lengthOne = len(stringOne)
    lengthTwo = len(stringTwo)
    maximum = 1

    if abs(lengthOne - lengthTwo) > 1:  # Check if each difference is 1
        return False

    if lengthTwo > lengthOne:
        for i in range(lengthOne):
            char1 = stringOne[i]
            char2 = stringTwo[i]

            if char1 != char2:
                if maximum > 0:
                    stringTwo = stringTwo[:i] + stringTwo[i + 1:]
                    # Same as deleting string[i] except python supports the code
                    maximum -= 1

                    if stringTwo[i] != char1:
                        return False
                else:
                    return False

    elif lengthTwo < lengthOne:
        for i in range(lengthTwo):
            char1 = stringOne[i]
            char2 = stringTwo[i]

            if char1 != char2:
                if maximum > 0:
                    stringOne = stringOne[:i] + stringOne[i + 1:]
                    # Same as deleting string[i] except python supports the code
                    maximum -= 1

                    if stringOne[i] != char2:
                        return False
                else:
                    return False

    elif lengthOne == lengthTwo:
        for i in range(lengthOne):
            char1 = stringOne[i]
            char2 = stringTwo[i]

            if char1 != char2:
                if maximum > 0:
                    maximum -= 1
                else:
                    return False

    else:
        return False
    return True