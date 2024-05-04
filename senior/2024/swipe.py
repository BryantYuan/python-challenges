total_num = int(input())
first = input()
steps = []
edited = first
target = input()
index = 0
succeed = True
prev = False
prev_index = 0
while index < total_num:
    cur = edited[index]
    correct = target[index]
    if cur != correct:

        if index != 0:
            if edited[index - 1] == correct:
                edited = edited[:index] + correct + edited[index + 1:]
                if prev:
                    steps[-1] = f'R {prev_index} {index}'
                else:
                    steps.append(f'R {index - 1} {index}')
                    prev_index = index - 1
                    prev = True
            else:
                prev = False

        if index + 1 != total_num:
            if edited[index + 1] == correct:
                edited = edited[:index] + correct + edited[index + 1:]
                steps.append(f'L {index} {index + 1}')

    cur = edited[index]
    if cur != correct:
        succeed = False
        break

    index += 1

prev = False
prev_index = 0
if not succeed:
    succeed = True
    index = total_num - 1
    while index > -1:
        cur = first[index]
        correct = target[index]
        if cur != correct:

            if index != 0:
                if first[index - 1] == correct:
                    first = first[:index] + correct + first[index + 1:]
                    if prev:
                        steps[-1] = f'L {prev_index} {index}'
                    else:
                        steps.append(f'L {index - 1} {index}')
                        prev_index = index - 1
                        prev = True
                else:
                    prev = False

            if index + 1 != total_num:
                if first[index + 1] == correct:
                    first = first[:index] + correct + first[index + 1:]
                    steps.append(f'R {index} {index + 1}')
        cur = first[index]
        if cur != correct:
            succeed = False
            break

        index -= 1

if not succeed:
    print('NO')
else:
    print('YES')
