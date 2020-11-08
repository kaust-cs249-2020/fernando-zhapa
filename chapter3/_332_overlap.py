import sys
sys.path.append("..")

from lib import printGraphAdjList, verticalPrint

from graph import fromAdjacencyList, hamiltonianPaths

def overlap(patterns):
    # Input: A collection Patterns of k-mers.
    # Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. (You may return the nodes and their edges in any order.)

    graph = {}
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            if i != j:
                if patterns[i][1:] == patterns[j][:-1]:
                    if patterns[i] in graph:
                        graph[patterns[i]].append(patterns[j])
                    else:
                        graph[patterns[i]] = [patterns[j]]
                    continue
    return graph

if __name__ == "__main__":
    
    file = open("data/overlap.txt", 'r')
    patterns = [line.rstrip('\n') for line in file]

    patterns = [

        
        "0000",
        "0001",
        "0010",
        "0011",
        "0100",
        "0101",
        "0110",
        "0111",
        "1000",
        "1001",
        "1010",
        "1011",
        "1100",
        "1101",
        "1110",
        "1111",
       
    ]

    adjacencyList = overlap(patterns)
    adjacencyMatrix = fromAdjacencyList(adjacencyList)
    paths = hamiltonianPaths(adjacencyMatrix,0)
