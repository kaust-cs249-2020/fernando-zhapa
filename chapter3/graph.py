def fromAdjacencyList(graph):
    # pass from adjacency list to adjacency matrix
    keys = [*graph.keys()]

    for values in graph.values():
        for value in values:
            if not value in keys:
                keys.append(value)
    n = len(keys)
    newValues = [i for i in range(n)]
    keysDict = dict(zip(keys,newValues))

    adjacencyMatrix = [[ 0 for i in range(n) ] for j in range(n)]

    for vertex, listNeighbors in graph.items():
        for neigh in listNeighbors:
            adjacencyMatrix[keysDict[vertex]][keysDict[neigh]] += 1
    return adjacencyMatrix






def auxCycles(graph, previous, next, start, adjacent=False):
    numberOfCycles = 0
    previous = previous[:]
    if next == start:
        if len(previous) == len(graph): # len(previous) > 2:
            print([x+1 for x in previous])
            return 1 #numberOfCycles +=1
        else:
            return 0
        
    if not next in previous:    
        previous.append(next)
        for nodeToExpand in range(len(graph)):
            if graph[next][nodeToExpand] == 1:
                numberOfCycles += auxCycles(graph,previous,nodeToExpand,start)
    return numberOfCycles
   


def hamiltonianCycles(graph, start):
    # computes the number of cycles that exist in a graph starting from a node "start"
    numberOfCycles = 0
    for i in range(len(graph[0])):
        if i != start and graph[start][i] == 1:
                numberOfCycles += auxCycles(graph,[start],i,start)
    return int(numberOfCycles/2)

def auxPaths(graph, previous, next, start, adjacent=False):
    numberOfPaths = 0
    previous = previous[:]

    if len(previous) == len(graph):
        print([x+1 for x in previous])
        return 1 #numberOfCycles +=1
    
    if next in previous:
       return 0
    else:    
        previous.append(next)
        for nodeToExpand in range(len(graph)):
            if graph[next][nodeToExpand] == 1:
                numberOfPaths += auxPaths(graph,previous,nodeToExpand,start)
    return numberOfPaths
   


def hamiltonianPaths(graph, start):
    # computes the number of paths that exist in a graph starting from a node "start"
    numberOfPaths = 0
    for i in range(len(graph[0])):
        if i != start and graph[start][i] == 1:
                numberOfPaths +=    (graph,[start],i,start)
    return numberOfPaths








if __name__ == "__main__":

    graph3 = [
        [0,1,1],
        [1,0,1],
        [1,1,0],
    ]

    graph = [
        [0,1,1,1],
        [1,0,1,1],
        [1,1,0,0],
        [1,1,0,0]
    ]

    graphKnight = [
        
        
        
        
        
        
        
        [0,0,0,0,0,1,1,0,1,0,0,0],
        [0,0,1,0,0,0,0,1,0,1,0,0],
        [0,1,0,0,0,0,0,0,1,0,1,0],
        [0,0,0,0,0,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,1,0,0,0,1,0],
        [1,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,1],
        [0,1,0,0,0,1,0,0,0,0,0,0],
        [1,0,1,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,0,0,0,0,0,0,1,0],
        [0,0,1,0,1,0,0,0,0,1,0,0],
        [0,0,0,1,0,1,1,0,0,0,0,0],

    ]   

    # total = 0
    # for i in range(len(graphKnight)):
    #     total += cycles(graphKnight,i)
    print(hamiltonianCycles(graphKnight,0))
    #print(total)

