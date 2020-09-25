
import copy

# MaximalNonBranchingPaths(Graph)
#         Paths ← empty list
#         for each node v in Graph
#             if v is not a 1-in-1-out node
#                 if out(v) > 0
#                     for each outgoing edge (v, w) from v
#                         NonBranchingPath ← the path consisting of single edge (v, w)
#                         while w is a 1-in-1-out node
#                             extend NonBranchingPath by the edge (w, u) 
#                              w ← u
#                         add NonBranchingPath to the set Paths
#         for each isolated cycle Cycle in Graph
#             add Cycle to Paths
#         return Paths



def readAdjacencyList(strings):
    graph = {}
    for string in strings:
        spplit = string.split(' -> ')
        key = int(spplit[0])
        value = [int(i) for i in spplit[1].split(',')]
        graph[key] = value
    return graph

def printPaths(paths):
    toPrint = ""
    for path in paths:
        path = [str(i) for i in path]
        toPrint = toPrint + ' -> '.join(path) + '\n'
    print(toPrint[:-1])

def is1In1OutNode(key, graph):

    if not key in graph:
        return False

    if len(graph[key]) != 1:
        return False

    incoming = 0
    for _ , values in graph.items():
        for i in range(len(values)):
            if values[i] == key:
                incoming+=1            
    if incoming == 1:
        return True
    else:
        return False
    

def outgoingEdges(key, graph):
    return graph[key]


def isolatedCycles(graph):
    cycles = []
    keys = [*graph.keys()]
    while bool(graph):
        for key in keys:
            if key in graph:
                cycle = [key]
                nextVertex = graph[key][0]
                del graph[key]
                
                while nextVertex != key:
                    cycle.append(nextVertex)
                    currVertex = nextVertex
                    nextVertex = graph[nextVertex][0]
                    del graph[currVertex]
                cycle.append(key)
                cycles.append(cycle)
    return cycles


def maximalNonBranchingPaths(graph):
    paths = []
    newGraph = copy.deepcopy(graph)
    for key in graph.keys():
        if not is1In1OutNode(key, graph):
            outgoing = outgoingEdges(key, graph)
            if len(outgoing) > 0:
                for outEdge in outgoing:
                    nonBranchingPath = [key,outEdge]
                    newGraph[key].remove(outEdge)
                    
                    while is1In1OutNode(outEdge, graph):

                        newOutgoingEdge = graph[outEdge][0]
                        newGraph[outEdge].remove(newOutgoingEdge)
                    
                        nonBranchingPath.append(newOutgoingEdge)
                        outEdge = newOutgoingEdge
                    paths.append(nonBranchingPath)
    
    newGraph = {key:val for key, val in newGraph.items() if val != []}

    paths += isolatedCycles(newGraph)

    return paths

if __name__ == "__main__":
    
    file = open("/home/ferynando7/KAUST/Fall2020/CS249/fernando-zhapa/data/maxNonBranchingPaths.txt", 'r')
    adjList = [line.rstrip('\n') for line in file]
    # adjList = [
    #     "1 -> 2",
    #     "2 -> 3",
    #     "3 -> 4,5",
    #     "6 -> 7",
    #     "7 -> 6",
    # ]

    graph = readAdjacencyList(adjList)
    printPaths(maximalNonBranchingPaths(graph))
