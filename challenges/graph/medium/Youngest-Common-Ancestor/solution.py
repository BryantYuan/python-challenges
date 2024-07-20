class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def defineDepth(descendant, ancestor):
    depth = 0
    while descendant != ancestor:
        descendant = descendant.ancestor
        depth += 1
    return depth


def getYoungestCommonAncestor(topAncestor: AncestralTree, descendantOne: AncestralTree, descendantTwo: AncestralTree):
    depth1 = defineDepth(descendantOne, topAncestor)
    depth2 = defineDepth(descendantTwo, topAncestor)

    while depth1 > depth2:
        descendantOne = descendantOne.ancestor
        depth1 -= 1

    while depth1 < depth2:
        descendantTwo = descendantTwo.ancestor
        depth2 -= 1

    while descendantOne != descendantTwo:
        print(descendantOne.name, descendantTwo.name)
        descendantTwo = descendantTwo.ancestor
        descendantOne = descendantOne.ancestor

    return descendantOne