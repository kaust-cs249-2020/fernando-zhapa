import numpy as np

def leavesDistance(tree, n):
    # Input: Tree and number of leaves
    # Output: Distance matrix

    distances = np.zeros((n,n))

    towardsRoot = []
    for i in range(n):
        towardsRoot.append(pathToRoot(tree, i))

    for i in range(n-1):
        for j in range(i+1,n):
            distances[i,j] = getDistance(towardsRoot[i], towardsRoot[j])
            distances[j,i] = distances[i,j]

    return distances

def pathToRoot(tree, leaf):
    parent, weight = tree[leaf]
    path = []
    prevWeight = 0    
    
    while parent != -1:
        path.append((parent, prevWeight+weight))
        
        node = parent
        prevWeight += weight
        parent, weight = tree[node]

    return path

def getDistance(path_i, path_j):
    cost = -1

    ancestorFound = False
    idx_i = 0
    idx_j = 0
    while not ancestorFound:
        parent_i, weight_i = path_i[idx_i]
        parent_j, weight_j = path_j[idx_j]
        
        if parent_i < parent_j:
            idx_i += 1
        elif parent_j < parent_i:
            idx_j += 1
        else:
            ancestorFound =  True
            cost = weight_i + weight_j

    return cost


def readTree(string_tree):
    tree = {}

    for line in string_tree:
        node, neighbor_info = tuple(line.split('->'))
        neighbor, weight = tuple(neighbor_info.split(':'))

        if not int(node) in tree:
            if int(node) > int(neighbor):
                tree[int(node)] = (-1,-1)
            else:
                tree[int(node)] = (int(neighbor), int(weight))
        else:
            if int(node) < int(neighbor):
                tree[int(node)] = (int(neighbor), int(weight))


    return tree

def spacedPrint(matrix):
    toPrint = ''
    for row in matrix:
        for elem in row:
            toPrint += str(int(elem)) + ' '
        toPrint = toPrint[:-1]
        toPrint += '\n'
    print(toPrint)



if __name__ == "__main__":
    
    file = open('data/leavesDistance.txt', 'r')

    num_leaves = int(file.readline().rstrip('\n'))

    string_tree =  file.readlines()

    tree = readTree(string_tree)

    distances = leavesDistance(tree, num_leaves)

    spacedPrint(distances)