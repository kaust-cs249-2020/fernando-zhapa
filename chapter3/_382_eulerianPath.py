import sys
sys.path.append('..')

from graph import fromAdjacencyList
from _381_eulerianCycle import eulerianCycle

def readAdjacencyList(strings):
    graph = {}
    for string in strings:
        spplit = string.split(' -> ')
        key = int(spplit[0])
        value = [int(i) for i in spplit[1].split(',')]
        graph[key] = value
    return graph


def findUnbalancedVertices(graph):
    start = -1
    end = -1
    keys = [*graph.keys()]
    for values in graph.values():
        for value in values:
            if not value in keys:
                keys.append(value)

    for key in keys:
        if not key in graph:
            outgoing = 0
        else:
            outgoing = len(graph[key])
        
        incoming = 0
        for key2, values in graph.items():
            if key in values:
                incoming+=1
        
        if outgoing > incoming:
            start = key
        elif incoming > outgoing:
            end = key
    return start, end


def eulerianPath(graph):
    # Input: The adjacency list of an Eulerian directed graph.
    # Output: An Eulerian path in this graph.
    
    start, end = findUnbalancedVertices(graph)
    if not end in graph:
        graph[end] = [start]
    else:
        graph[end].append(start)

    path = eulerianCycle(graph,start=start)
    
    for i in range(len(path)):
        if path[i] == end:
            path = path[i+1:-1] + path[:i+1]
            break

    return path


if __name__ == "__main__":
    file = open("data/eulerPath.txt", 'r')
    
    strings = [line.rstrip('\n') for line in file]

    graph = readAdjacencyList(strings)
    cycle = eulerianPath(graph)
    cycleToStr = [str(i) for i in cycle]
    print('->'.join(cycleToStr))


