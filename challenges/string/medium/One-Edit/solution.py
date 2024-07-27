def oneEdit(stringOne, stringTwo):
    lengthOne = len(stringOne)
    lengthTwo = len(stringTwo)

    if abs(lengthOne - lengthTwo) == 1:  # Check if each difference is 1
        maximum = 1

        # If len2 is larger, it used remove, so we go for len1 or else there will be out of range error.
        for i in range(lengthOne if lengthTwo > lengthOne else lengthTwo):
            char1 = stringOne[i]
            char2 = stringTwo[i]

            if char1 != char2:
                if maximum > 0:
                    del stringTwo[i]
                    maximum -= 1

                    if stringTwo[i] != char1:
                        return False
                else:
                    return False
            else:
                return False

    elif lengthOne == lengthTwo:
        maximum = 1
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