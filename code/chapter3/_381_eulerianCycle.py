import sys
sys.path.append('..')

# from lib import readAdjacencyList

def readAdjacencyList(strings):
    graph = {}
    for string in strings:
        spplit = string.split(' -> ')
        key = int(spplit[0])
        value = [int(i) for i in spplit[1].split(',')]
        graph[key] = value
    return graph


def redefineCycle(cycle, newStart):
    #receives a list of elements forming a cycle and a vertex that will be the new starting point
    beforeNewStart = []
    cycle = cycle[1:]
    for i in range(len(cycle)):
        vertex = cycle[i]
        if vertex == newStart:
            beforeNewStart.append(newStart)
            return (cycle[i:] + beforeNewStart)
        else:
            beforeNewStart.append(cycle[i])

def eulerianCycle(graph,start=-1,end=-1):
    # Input: The adjacency list of an Eulerian directed graph.
    # Output: An Eulerian cycle in this graph.
    start = next(iter(graph))
    currNode = start
    cycle = [start]
    while bool(graph): #the graph has remaining edges
        if not currNode in graph: #non Eulerian cycle
            for vertex in cycle: #look for new start
                if vertex in graph:
                    start = vertex
                    cycle = redefineCycle(cycle,start)
                    currNode = start
        possibleVertices = graph[currNode]
        if len(possibleVertices) == 1:
            nextNode = possibleVertices[0]
            del graph[currNode]
        else:
            nextNode = possibleVertices[0]
            graph[currNode].remove(nextNode)
        cycle.append(nextNode)
        currNode = nextNode
    return cycle


if __name__ == "__main__":
    file = open("/home/ferynando7/KAUST/Fall2020/CS249/fernando-zhapa/data/eulerCycle.txt", 'r')
    
#    file = open("../../data/eulerCycle.txt", 'r')
    strings = [line.rstrip('\n') for line in file]

    graph = readAdjacencyList(strings)
    cycle = eulerianCycle(graph)
    cycleToStr = [str(i) for i in cycle]
    print('->'.join(cycleToStr))


