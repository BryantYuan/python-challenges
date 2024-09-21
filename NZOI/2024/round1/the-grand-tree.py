"""Time has come to pick the apples from The Grand Tree. The Grand Tree has N apples
numbered 0 to N−1, and N−1 branches. Each branch connects two different apples. Any
two apples are connected by exactly one sequence of branches. Each apple has a
tastiness level that you, as a skilled apple picker, can determine just by looking at
it. Unfortunately, The Grand Tree is rather Grand™, which means that you can only pick
an apple by climbing up to it. Even more unfortunately, you are a bit clumsy, and
cannot climb past an apple without knocking it off and damaging it. As such, you can
climb along the branches to reach any apples you want, but you must pick every apple
you climb past on the way. The trunk of the tree is located at apple 0, meaning you
always start there, and you must pick apple 0 in order to begin climbing the tree.
You may always pick apple 0.

You have decided ahead of time that you wish to harvest a selection of apples where
the sum of the tastiness of all the apples you have picked is equal to M.
You however, are aware that that might not always be possible, so you have decided
to settle for the smallest possible sum of tastiness greater than or equal to M.
Due to the staggering size of the tree, you cannot work out which apples to pick in
your head, and thus have decided to sit down and write a program instead."""
import sys


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.next = []


applesAmount, target_value = tuple(map(int, input().split(' ')))  # Turns it into an int
allApples = input().split(' ')
sys.setrecursionlimit(100000)

root = BinaryTree(int(allApples[0]))
allNodes = [root]
for apple in allApples[1:]:
    allNodes.append(BinaryTree(int(apple)))

for i in range(applesAmount - 1):
    branch1, branch2 = tuple(map(int, input().split(' ')))
    allNodes[branch1].next.append(allNodes[branch2])


class Result:
    def __init__(self, flag, value):
        self.flag = flag  # 0: Found, perfect, 1: Found, but unsure if it is the best
        self.value = value


def pickApples(_root: BinaryTree, currentSum):
    closest_taste = -1

    newSum = currentSum + _root.value
    if newSum == target_value:
        return Result(0, newSum)
    if newSum > target_value:
        return Result(1, newSum)

    nextNodes = _root.next
    for nextVal in nextNodes:
        applesCollected = pickApples(nextVal, newSum)
        if applesCollected.flag == 0:
            return Result(0, applesCollected.value)
        if applesCollected.flag == 1:
            if closest_taste == -1 or applesCollected.value < closest_taste:
                closest_taste = applesCollected.value

    closest_taste = closest_taste if closest_taste != -1 else newSum
    return Result(2, closest_taste)


print(pickApples(root, 0).value)