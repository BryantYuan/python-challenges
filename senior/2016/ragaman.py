original = input()
asterisk = input()
fail = False

for char in asterisk:
    if char == '*':
        continue
    if char in original:
        original = original.replace(char, '', 1)
    else:
        fail = True

if not fail:
    print('A')
else:
    print('N')
