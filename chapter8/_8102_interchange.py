from _891_smallParsimony import hammingDistance
from _892_smallParsimonyUnrooted import buildTree, isInt, smallParsimonyUnrooted, restartTags
from math import ceil
from reprlib import recursive_repr
from copy import deepcopy



def unroot(tree):
    tree = deepcopy(tree)
    if tree.label == 'ROOT':
        daughter = tree.daughter
        son = tree.son
        return {daughter.value: daughter, son.value: son}
    else:
        return "No valid for unroot"


def scoreNodes(nodes):
    nodes = list(nodes.items())

    val1, node1 = nodes[0]
    val2, node2 = nodes[1]

    return {val1: node1.totalScore(), val2: node2.totalScore()}

def nearestNeighbors(nodes):
    nodes = list(nodes.items())

    val1, node1 = nodes[0]
    val2, node2 = nodes[1]


    node1Aux = deepcopy(node1)

    newNode1 = deepcopy(node1)
    newNode2 = deepcopy(node2)

    newNode1.son = deepcopy(newNode2.daughter)
    newNode2.daughter = deepcopy(node1Aux.son)

    neigh1 = {val1: newNode1, val2: newNode2}

 
    node1Aux = deepcopy(node1)

    newNode1 = deepcopy(node1)
    newNode2 = deepcopy(node2)

    newNode1.son = deepcopy(newNode2.son)
    newNode2.son = deepcopy(node1Aux.son)

    neigh2 = {val1: newNode1, val2: newNode2}
    return [neigh1, neigh2]



def nextEdges(nodes):

    newTrees = []
    nodes = list(nodes.items())

    val1, node1 = nodes[0]
    val2, node2 = nodes[1]

    # First change
    newNode1 = deepcopy(node1)
    newNode2 = deepcopy(node2)

    if not newNode1.daughter.isLeaf():
        subTree1 = newNode1.daughter
        newNode1.daughter = newNode2
        subTree2 = newNode1
        
        newNodes =  {subTree1.value: subTree1, subTree2.value: subTree2}

        newTrees.append(newNodes)

    # Second change
    newNode1 = deepcopy(node1)
    newNode2 = deepcopy(node2)

    if not newNode1.son.isLeaf():
        subTree1 = newNode1.son
        newNode1.son = newNode2
        subTree2 = newNode1
        
        newNodes =  {subTree1.value: subTree1, subTree2.value: subTree2}

        newTrees.append(newNodes)

    # Third change
    newNode1 = deepcopy(node1)
    newNode2 = deepcopy(node2)

    if not newNode2.daughter.isLeaf():
        subTree1 = newNode2.daughter
        newNode2.daughter = newNode1
        subTree2 = newNode2
        
        newNodes =  {subTree1.value: subTree1, subTree2.value: subTree2}

        newTrees.append(newNodes)

    # Fourth change
    newNode1 = deepcopy(node1)
    newNode2 = deepcopy(node2)
    if not newNode2.son.isLeaf():
        subTree1 = newNode2.son
        newNode2.son = newNode1
        subTree2 = newNode2
        
        newNodes =  {subTree1.value: subTree1, subTree2.value: subTree2}

        newTrees.append(newNodes)

    return newTrees


# There are O(2n) edges, n is the number of leaves
# O(m*n^2) * O(2n)
def checkInternalEdges(tree, num_leaves, len_seq, score, explored):
    nodes = deepcopy(tree)
 
    nodesValues = [*nodes.keys()]
    nodesValues.sort()
    if nodesValues in explored:
        return nodes, float('inf')

   
    neighs = nearestNeighbors(nodes)
    minTree = tree
    minScore = score

    # O(2*m*n^2)
    for neigh in neighs:
        newTree = smallParsimonyUnrooted(neigh, len_seq)
        newScore = newTree.totalScore()
    
        if newScore < minScore:
            minTree = newTree
            minScore = newScore

    explored.append(nodesValues)


    newUnrootedTrees = nextEdges(nodes) #Returns at most 4 new trees

    for unrootedTree in newUnrootedTrees:

        newTree =  smallParsimonyUnrooted(unrootedTree, len_seq)
        newScore = newTree.totalScore()
        if newScore < minScore:
            minTree = newTree
            minScore = newScore

        newTree, newScore = checkInternalEdges(unrootedTree, num_leaves, len_seq, minScore, explored)
        if newScore < minScore:
            minTree = newTree
            minScore = newScore
    
    return minTree, minScore



def interchange(adjList, num_leaves, len_seq):
    score  = float('inf')

    # O(2n)
    nodes = buildTree(adjList, num_leaves)
    
    # O(m*n^2)
    tree = smallParsimonyUnrooted(nodes, len_seq)

    newScore = tree.totalScore()


    while newScore < score:
        print(newScore)
        print(tree)
        score = newScore
        tree, newScore = checkInternalEdges(unroot(tree), num_leaves, len_seq, score, [])


    return tree, newScore


if __name__ == "__main__":
    
    file =  open('data/interChange.txt', 'r')

    n = int(file.readline().rstrip('\n'))
    
    edges =  [tuple(line.rstrip('\n').split('->')) for line in file]

    x, y = edges[0]
    if not isInt(x):
        m = len(x)
    elif not isInt(y):
        m = len(y)
    else:
        m = "ERROR"
    
    
    nodes, score = interchange(edges, n, m)


