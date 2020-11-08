import numpy as np

# NeighborJoining(D)
#     n ← number of rows in D
#     if n = 2
#         T ← tree consisting of a single edge of length D1,2
#         return T
#     D* ← neighbor-joining matrix constructed from the distance matrix D
#     find elements i and j such that D*i,j is a minimum non-diagonal element of D*
#     Δ ← (TotalDistanceD(i) - TotalDistanceD(j)) /(n - 2)
#     limbLengthi ← (1/2)(Di,j + Δ)
#     limbLengthj ← (1/2)(Di,j - Δ)
#     add a new row/column m to D so that Dk,m = Dm,k = (1/2)(Dk,i + Dk,j - Di,j) for any k
#     D ← D with rows i and j removed
#     D ← D with columns i and j removed
#     T ← NeighborJoining(D)
#     add two new limbs (connecting node m with leaves i and j) to the tree T
#     assign length limbLengthi to Limb(i)
#     assign length limbLengthj to Limb(j)
#     return T

class Node():
    def __init__(self, value, children=[]):
        self._value = value
        self._children = children

    def __repr__(self):
        string = ''
        for child, weight in self._children:
            string += str(self._value) + '->' + str(child) + ':' + "{:.2f}".format(weight) + '\n'
            string += str(child) + '->' + str(self._value) + ':' + "{:.2f}".format(weight) + '\n'
        return string[:-1]
    



# O(n^2) * O(n) | the latter is for recursion
def neighborJoining(distanceMatrix, num_leaves, indicesMap):
    n = len(    )

    if n==2:
        i = get_key(0, indicesMap)
        j = get_key(1, indicesMap)
        newNode =  Node(i, children=[(j,distanceMatrix[0,1])])
        return {1: newNode}

    newNodeLabel = num_leaves
    
    # O(n^2)
    neighJoinMatrix = neighborJoiningMatrix(distanceMatrix)

    # O(n^2)
    i, j = indicesMinDistance(neighJoinMatrix, indicesMap)

    
    f_i = indicesMap[i]
    f_j = indicesMap[j]

    # O(n)
    delta = (totalDistance(distanceMatrix, f_i) - totalDistance(distanceMatrix, f_j)) / (n-2)

    limbLength_i = (distanceMatrix[f_i,f_j] + delta)/2
    limbLength_j = (distanceMatrix[f_i,f_j] - delta)/2

    # O(n)
    col_new = getNewCol(distanceMatrix, f_i, f_j)

    distanceMatrix, indicesMap =  updateMatrix(distanceMatrix, i, j, newNodeLabel, col_new, indicesMap)

    tree = neighborJoining(distanceMatrix, num_leaves+1, indicesMap)

    newNode =  Node(newNodeLabel, children=[(i, limbLength_i), (j, limbLength_j)])

    tree[newNodeLabel] =  newNode

    return tree


# O(n^2)
def neighborJoiningMatrix(distanceMatrix):
    n = len(distanceMatrix)
    neighJoinMatrix = np.copy(distanceMatrix)

    for i in range(0,n-1):
        for j in range(i+1, n):
            neighJoinMatrix[i,j] = (n-2) * distanceMatrix[i,j] - totalDistance(distanceMatrix, i) - totalDistance(distanceMatrix, j)
            neighJoinMatrix[j,i] = neighJoinMatrix[i,j]
    return neighJoinMatrix

def updateMatrix(distanceMatrix, i, j, newNodeLabel, col_new, indicesMap):
    
    f_i = indicesMap[i]
    f_j = indicesMap[j]
     # remove ci and cj from matrix
    distanceMatrix = np.delete(distanceMatrix, [f_i, f_j], axis= 0)
    distanceMatrix = np.delete(distanceMatrix, [f_i, f_j], axis= 1)

    rowToAdd = np.expand_dims(col_new,axis=0)

    # extend matrix
    distanceMatrix = np.vstack((distanceMatrix, rowToAdd))
    col_new = np.append(col_new, 0)
    colToAdd = np.expand_dims(col_new,axis=1)
    distanceMatrix = np.hstack((distanceMatrix, colToAdd))

    del indicesMap[i]
    del indicesMap[j]
    # indices.remove(ci)
    # indices.remove(cj)
    indicesMap[newNodeLabel] = float('inf')
    sorted_indices =  {k: v for k, v in sorted(indicesMap.items(), key=lambda item: item[1])}
    i=0
    for key,_ in sorted_indices.items():
        sorted_indices[key] = i
        i+=1

    return distanceMatrix, sorted_indices

# O(n^2)
def indicesMinDistance(matrix, indicesMap):
    n = len(matrix)
    minDistance = float('inf')
    for i in range(0, n-1):
        for j in range(i+1,n):
            if matrix[i,j] < minDistance:
                minDistance = matrix[i,j]
                pair = (i,j)
    i, j = pair
    i =  get_key(i, indicesMap)
    j = get_key(j, indicesMap)
    return i, j

def get_key(val, dict): 
    for key, value in dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

# O(|rows matrix|)
def totalDistance(matrix, i):
    return sum(matrix[:,i])

def getNewCol(matrix, i, j):
    newCol = []

    for k in range(len(matrix)):
        value = (matrix[k,i] + matrix[k,j] - matrix[i,j])/2
        newCol.append(value)

    newCol = np.array(newCol)
    newCol = np.delete(newCol, [i,j])

    return newCol


if __name__ == "__main__":
    
    file = open('data/neighborJoining.txt', 'r')

    n = int(file.readline().rstrip('\n'))

    matrix = np.array([[int(i) for i in line.split(' ')] for line in file])

    indices = {i:i for i in range(n)}

    tree = neighborJoining(matrix, n, indices)

    for key, node in tree.items():
        print(node)
