import collections

numberOfPineCones, numberOfScenarios = input().split()
numberOfPineCones = int(numberOfPineCones)
listOfPineCones = input().split()
listOfScenarios = []

for i in range(int(numberOfScenarios)):
    listOfScenarios.append(int(input()))


def getNumbers(_scenario, numberOfPineCones, listOfPineCones):
    # Unittest Done, 100%.
    if _scenario >= numberOfPineCones:
        listOfPineCones.sort()
        stack = collections.deque()  # A real stack not a list!
        for pinecone in listOfPineCones:
            stack.append(int(pinecone))

    else:
        stack = collections.deque([-1 for i in range(_scenario)])
        for pinecone in listOfPineCones:
            first_val = stack[0]  # Stack top value
            pinecone = int(pinecone)
            if pinecone > first_val:
                stack[0] = pinecone  # Replace top val

                for i in range(1, _scenario):  # 2nd val to the end
                    if pinecone > stack[i]:
                        stack[i - 1] = stack[i]
                        stack[i] = pinecone
    return stack


def findValue(stack, scenario, length):
    total_val = 0
    for i in range(scenario):
        cur_val = stack[-1]

        for j in range(length - 2, -1, -1):  # Go backwards
            if cur_val < stack[j]:
                stack[j + 1] = stack[j]
                stack[j] = cur_val
            else:
                break

        largest_val = stack[-1]

        if largest_val == 0:
            break

        total_val += largest_val
        stack[-1] -= 1

    return total_val


for scenario in listOfScenarios:
    new_stack = getNumbers(scenario, numberOfPineCones, listOfPineCones)
    print(findValue(new_stack, scenario,
                    numberOfPineCones if scenario > numberOfPineCones else scenario))