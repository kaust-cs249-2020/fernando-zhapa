import numpy as np

class Node():
    def __init__(self, value, age=0, children=[]):
        self._value = value
        self._age = age
        self._children = children
    
    def getAge(self):
        return self._age

    def getValue(self):
        return self._value
    
    def isLeaf(self):
        if self._children == []:
            return True
        else:
            return False

    def __repr__(self):
        toPrint = ''
        if self._children == []:
            toPrint += ''
        else:
            for child in self._children:
                weight = self._age - child.getAge()
                toPrint += str(self._value) + '->' + str(child.getValue()) + ':' + str() + "{:.2f}".format(weight) + '\n'
                toPrint += str(child.getValue()) + '->' + str(self._value) + ':' + str() + "{:.2f}".format(weight) + '\n'

        return toPrint[:-1]

def get_key(val, dict): 
    for key, value in dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def distanceClusters(c1,c2, originMatrix):
    n = len(originMatrix)
    leafs_c1 = [i for i in c1 if i >= 0 and i < n]
    leafs_c2 = [i for i in c2 if i >= 0 and i < n]

    sum = 0
    for elem1 in leafs_c1:
        for elem2 in leafs_c2:
            sum += matrix[elem1,elem2]
    return sum/(len(leafs_c1) * len(leafs_c2))

def closestClusters(clusters, indices, originMatrix):
    distance = float('inf')
    pair = None
    for i in range(len(clusters)-1):
        for j in range(i+1, len(clusters)):
            ci = get_key(i, indices) 
            cj = get_key(j, indices)
            candidateDistance = distanceClusters(clusters[ci], clusters[cj], originMatrix)
            #candidateDistance = distanceClusters(matrix[i], matrix[j], matrix) 
            if candidateDistance < distance:
                distance = candidateDistance
                pair = (ci,cj)
    ci, cj = pair
    return ci, cj, distance

def updateMatrix(matrix, indices, ci, cj, cNew):
    col_i =  matrix[:,indices[ci]]
    col_j =  matrix[:,indices[cj]]

    # remove positions that corresponds to the diagonal positions in each array
    zero_i =  np.where(col_i==0)[0][0]
    col_i = np.delete(col_i,zero_i)
    col_j = np.delete(col_j,zero_i)
    # col_i.pop(zero_i)
    # col_j.pop(zero_i)

    zero_j =  np.where(col_j==0)[0][0]
    col_i = np.delete(col_i,zero_j)
    col_j = np.delete(col_j,zero_j)
    # col_i.pop(zero_j)
    # col_j.pop(zero_j)


    # remove ci and cj from matrix
    matrix = np.delete(matrix,[indices[ci],indices[cj]], axis= 0)
    matrix = np.delete(matrix,[indices[ci],indices[cj]], axis= 1)

    col_new =  np.add(col_i,col_j)/2
    rowToAdd = np.expand_dims(col_new,axis=0)

    # extend matrix
    matrix = np.vstack((matrix, rowToAdd))
    col_new = np.append(col_new, 0)
    colToAdd = np.expand_dims(col_new,axis=1)
    matrix = np.hstack((matrix, colToAdd))
    
    # update indices
    del indices[ci]
    del indices[cj]
    # indices.remove(ci)
    # indices.remove(cj)
    indices[cNew] = float('inf')
    sorted_indices =  {k: v for k, v in sorted(indices.items(), key=lambda item: item[1])}
    i=0
    for key,_ in sorted_indices.items():
        sorted_indices[key] = i
        i+=1

    return matrix, sorted_indices



    

def upgma(matrix, n):
    # Input: An integer n followed by a space separated n x n distance matrix.
    # Output: An adjacency list for the ultrametric tree returned by UPGMA. Edge weights should be accurate to two decimal places (answers in the sample dataset below are provided to three decimal places).
    firstMatrix = np.copy(matrix)
    clusters = {i:[i] for i in range(n)}
    indices = {i:i for i in range(n)}
    graph = {i: Node(i) for i in range(n)}
    idxNewCluster = n
    while bool(clusters):
        idx_ci, idx_cj, distance = closestClusters(clusters, indices, firstMatrix)
        ci = clusters[idx_ci]
        cj = clusters[idx_cj]
     
        # update clusters
        cNew = ci + cj
        del clusters[idx_ci]
        del clusters[idx_cj]
        # clusters.remove(ci)
        # clusters.remove(cj)
        clusters[idxNewCluster] = cNew

        if len(clusters) == 1:
            clusters = {}
        
        #Update graph
        node_cNew = Node(idxNewCluster, age = distance/2 ,children=[graph[idx_ci], graph[idx_cj]])
        graph[idxNewCluster] = node_cNew

        #updateMatrix
        matrix, indices =  updateMatrix(matrix, indices, idx_ci, idx_cj, idxNewCluster)
        idxNewCluster += 1
    return graph

if __name__ == "__main__":
    
    file = open('data/upgma.txt', 'r')

    n = int(file.readline().rstrip('\n'))

    matrix = np.array([[int(i) for i in line.split(' ')] for line in file])

    tree = upgma(matrix, n)
    
    for key, node in tree.items():
        if not node.isLeaf():
            print(node)