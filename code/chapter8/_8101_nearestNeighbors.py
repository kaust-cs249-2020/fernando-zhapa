from copy import deepcopy
def nearestNegihbors(i, j, adjList):
    num_neighs_i = 0
    neighs_i = []
    for source, target in adjList:
        if source == i and target != j:
            neighs_i.append((source, target))
            num_neighs_i +=1
        
        if num_neighs_i == 2:
            break
    
    for source, target in neighs_i:
        adjList.remove((source, target))
        adjList.remove((target, source))

    
    num_neighs_j = 0
    neighs_j = []
    for source, target in adjList:
        if source == j and target != i:
            neighs_j.append((source, target))
            num_neighs_j +=1
        
        if num_neighs_j == 2:
            break
    
    for source, target in neighs_j:
        adjList.remove((source, target))
        adjList.remove((target, source))

    
    adjList_1 = deepcopy(adjList)

    adjList_1.append((neighs_i[0][1],i))
    adjList_1.append((i,neighs_i[0][1]))

    adjList_1.append((neighs_j[0][1],i))
    adjList_1.append((i,neighs_j[0][1]))

    adjList_1.append((neighs_i[1][1],j))
    adjList_1.append((j,neighs_i[1][1]))

    adjList_1.append((neighs_j[1][1],j))
    adjList_1.append((j,neighs_j[1][1]))



    adjList_2 = deepcopy(adjList)

    adjList_2.append((neighs_i[0][1],i))
    adjList_2.append((i,neighs_i[0][1]))

    adjList_2.append((neighs_j[1][1],i))
    adjList_2.append((i,neighs_j[1][1]))

    adjList_2.append((neighs_j[0][1],j))
    adjList_2.append((j,neighs_j[0][1]))

    adjList_2.append((neighs_i[1][1],j))
    adjList_2.append((j,neighs_i[1][1]))

    return adjList_1, adjList_2

def printAdjList(adjList):
    string = ''
    for i, j in adjList:
        string += i + '->' + j + '\n'
    print(string)

if __name__ == "__main__":
    file = open('data/nearestNeightbor.txt', 'r')

    i, j = tuple(file.readline().rstrip('\n').split(' '))

    adjList = [tuple(line.rstrip('\n').split('->')) for line in file]

    adjList1, adjList2 = nearestNegihbors(i,j, adjList)

    printAdjList(adjList1)
    printAdjList(adjList2)