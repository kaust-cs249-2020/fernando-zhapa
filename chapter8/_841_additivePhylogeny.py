from _831_limbLength import limbLength
from copy import deepcopy
import numpy as np
import os
from node import Node

# def doubleEdgesAditivePhylogeny(matrix, num_leaves):
#     tree = additivePhylogeny(matrix,num_leaves)
#     newTree = deetree
#     for node, neighbor, weight in tree:
#         newTree.append((neighbor,node, weight))
    
#     return newTree

def additivePhylogeny(matrix, num_leaves):

  
    n = len(matrix)

    if n==2:


        weight = matrix[0,1]
        node = Node(0,(1,weight))
        root = Node(1)
        root.insertChild(0,weight)
        return {0:node, 1:root}

    limbLen = limbLength(n,n-1,matrix) # n-1 is the last position

    for i in range(n-1):
        matrix[n-1,i] -= limbLen
        matrix[i,n-1] -= limbLen
    
    leaf1, leaf2 = baldLimbInfo(n,n-1,matrix)
    distance_leaf1 = matrix[leaf1,n-1]


    shortMatrix =  matrix[:n-1,:n-1]
    tree = additivePhylogeny(shortMatrix, num_leaves)

    pathLeaf1_2 = path(pathToRoot(tree,leaf1), pathToRoot(tree,leaf2))

    tree = attachLimb(pathLeaf1_2, distance_leaf1, n-1, limbLen, tree, num_leaves)

    return tree



def pathToRoot(tree, leaf):
    parent = tree[leaf].getParent()
    path = [(leaf,0)]
    prevWeight = 0    
    
    while parent != None:
        parentVal, weight = parent
        path.append((parentVal, prevWeight+weight))
        
        node = parentVal
        prevWeight += weight
        parent = tree[node].getParent()

    return path

def path(path_i, path_j):
    ancestorFound = False
    i = 0
    j = 0

    while not ancestorFound:
        parent_i, _ = path_i[i]
        j = 0
        while not ancestorFound and j < len(path_j):
        
            parent_j, _ = path_j[j]

            if parent_i == parent_j:
                ancestorFound = True
            
            j += 1
        
        i += 1

    path_i = path_i[:i]
    _,weight_i = path_i[-1]
    path_j = path_j[:j][::-1]

    for i in range(1, len(path_j)):
        _,weight_i = path_i[-1]
        newNode, weight = path_j[i] 
        _, weight2 = path_j[i-1] 
        path_i.append((newNode, weight2-weight+weight_i))
    return path_i


# def path(leaf1, leaf2, tree):


# def baldLimb(matrix):
#     n = len(matrix)
#     limbLen, distance_i, distance_j, leaf_i, leaf_j =  baldLimbInfo(n,n-1, matrix)

#     if limbLen == 0:
#         return leaf_i, leaf_j, distance_i, distance_j
#     else:
#         return "error in baldLimb"

def baldLimbInfo(n, j, matrix):
    found = False
    i = 0
    pair = (-1,-1)
    while not found and i<n-2:
        k = i+1
        while not found and k<n-1:
            if i != j and k != j:
                limb_length_j = (matrix[i,j] + matrix[j,k] - matrix[i,k])/2
                if limb_length_j == 0:
                    pair = (i,k)
                    found = True
            k+=1
        i+=1

    return pair



def attachLimb(pathLeaf1_2, distance_leaf1, newLeaf, limbLen, tree, num_leaves):

    for i in range(1,len(pathLeaf1_2)):
        node, weight = pathLeaf1_2[i]


        if weight == distance_leaf1:
            newNode = Node(newLeaf, (node, limbLen))
            tree[node].insertChild(newNode,limbLen)
            tree[newLeaf] = newNode
            break   
        if weight > distance_leaf1:
            newNode =  maxNode(tree, num_leaves)
            prev_node, prev_weight = pathLeaf1_2[i-1]

            removed1 = tree[node].dropConnection(prev_node)
            removed2 = tree[prev_node].dropConnection(node)

            if removed1 == 'parent' and removed2 == 'parent':
                tree[newNode] = Node(newNode)
                tree[newNode].insertChild(node,weight-distance_leaf1)
                tree[newNode].insertChild(prev_node,distance_leaf1 - prev_weight)
                tree[newNode].insertChild(newLeaf,limbLen)
                
                tree[node].setParent(newNode,weight-distance_leaf1)
                tree[prev_node].setParent(newNode, distance_leaf1 - prev_weight)
            elif removed1 == 'parent' and removed2 == 'children':
                tree[newNode] = Node(newNode, (prev_node,distance_leaf1 - prev_weight))
                tree[newNode].insertChild(node,weight-distance_leaf1)
               # tree[newNode].insertChild(prev_node,distance_leaf1 - prev_weight)
                tree[newNode].insertChild(newLeaf,limbLen)
                
                tree[node].setParent(newNode,weight-distance_leaf1)
                tree[prev_node].insertChild(newNode, distance_leaf1 - prev_weight)
            elif removed2 == 'parent' and removed1 == 'children':
                tree[newNode] = Node(newNode, (node,weight-distance_leaf1))
                tree[newNode].insertChild(prev_node,distance_leaf1 - prev_weight)
                tree[newNode].insertChild(newLeaf,limbLen)
                
                tree[prev_node].setParent(newNode,distance_leaf1 - prev_weight)
                tree[node].insertChild(newNode, weight-distance_leaf1)
            else:
                return "error in attach limb"
            newLeafNode = Node(newLeaf, (newNode, limbLen))
            tree[newLeaf] = newLeafNode
            break
    return tree    

def maxNode(tree, num_leaves):
    maximum =  float('-inf')
    for label, node in tree.items():
        candidate =  node.maxNode()
        if candidate > maximum:
            maximum = candidate

    if  maximum >= num_leaves:
        return maximum +1
    else:
        return num_leaves

def root(tree, leaf):
    parent, weight = getParentAndWeight(tree, leaf)
    path = []
    prevWeight = 0    
    
    while parent != None:
        path.append((parent, prevWeight+weight))
        
        node = parent
        prevWeight += weight
        parent, weight = getParentAndWeight(tree, node)

    return path[-2:]


def getParentAndWeight(tree, node):
    parent = float('inf')
    weight = -1
    for node_candidate, parent_candidate, weight_candidate in tree:
        if node == node_candidate and parent_candidate > node:
            if parent_candidate < parent:
                parent = parent_candidate
                weight = weight_candidate
        # else:
        #     parent = -1
        #     weight = -1
    if parent == float('inf'):
        parent = -1
    return parent, weight

# def path(path_i, path_j):
#     cost = -1
#     ancestorFound = False
#     idx_i = 0
#     idx_j = 0
#     while not ancestorFound:
#         parent_i, weight_i = path_i[idx_i]
#         parent_j, weight_j = path_j[idx_j]
        
#         if parent_i < parent_j:
#             idx_i += 1
#         elif parent_j < parent_i:
#             idx_j += 1
#         else:
#             ancestorFound =  True
#             cost = weight_i + weight_j
#     return parent_i, cost


def printTree(tree):
    toPrint = ''
    for _, node in tree.items():
        toPrint += node.adjacencyListString()
    print(toPrint)
if __name__ == "__main__":
    
    file = open(os.getcwd() + '/data/additivePhylogeny.txt', 'r')

    n = int(file.readline().rstrip('\n'))

    matrix = np.array([[int(i) for i in line.split(' ')] for line in file])
  
    printTree(additivePhylogeny(matrix,n))