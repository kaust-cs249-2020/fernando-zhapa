from collections import OrderedDict
import os
import copy

def longestPathDAG(start,end,predecessors):

    # predecessors have the form {node_b: [(node_a, weight_ab),....]}

    backtrackArray = {i: -1 for i in range(start,end+1)}

    distances = {i: 0 for i in range(start,end+1)}

    predecessors = OrderedDict(sorted(predecessors.items())) 


    for node, incomingNodes in predecessors.items():

        maxDistance = float('-inf')
        for inc_node, weight  in incomingNodes:
            if inc_node in predecessors.keys():
                candidateDistance = distances[inc_node] + weight 
                if candidateDistance > maxDistance:
                    maxDistance = candidateDistance
                    distances[node] = candidateDistance
                    backtrackArray[node] = inc_node

    path = []

    currNode = end
    while currNode != start and currNode != -1:
        path.append(currNode)
        currNode = backtrackArray[currNode]

    if currNode == start:
        path.append(currNode)
    
    path.reverse()

    return distances[end], path


def processEdges(start, end, edges):

    predecessors = {i:[] for i in range(start, end+1)}

    for edge in edges:
        origin, destNWeight = tuple(edge.split('->'))
        dest, weight = tuple(destNWeight.split(':'))
        predecessors[int(dest)].append((int(origin), int(weight)))

    # delete no-incoming-edges nodes
    no_incoming_edges = 0
    existIncoming = True
    
    while existIncoming:
        newDict = {}
        no_incoming = []
        for key, value in predecessors.items():
            if value == [] and key != start:
                no_incoming.append(key)
                no_incoming_edges +=1
            else:
                newDict[key] = value
  
        if no_incoming_edges == 0:
            existIncoming = False
        else:
            predecessors = copy.deepcopy(newDict)
            for key, value in newDict.items():
                valueCopy = value[:]
                for (n,w) in valueCopy:
                    if n in no_incoming:
                        predecessors[key].remove((n,w))
            no_incoming_edges = 0

    return newDict

def prettyPrint(longestPathOutput):
    distance, path = longestPathOutput
    toPrint = str(distance) + '\n'
    
    for item in path:
        toPrint += str(item) + '->'

    print(toPrint[:-2])


if __name__ == "__main__":
    
    #os.getcwd() + '/code/chapter5/' + 
    file = open('data/longestPathDAG.txt', 'r')

    start = int(file.readline().rstrip('\n'))
    end = int(file.readline().rstrip('\n'))

    edges = []

    edge = file.readline().rstrip('\n')

    while edge != "":
        edges.append(edge)
        edge = file.readline().rstrip('\n')

    predecessors = processEdges(start, end, edges)

    prettyPrint(longestPathDAG(start, end, predecessors))