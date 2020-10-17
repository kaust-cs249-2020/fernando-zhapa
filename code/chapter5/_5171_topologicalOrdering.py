from copy import deepcopy
# TopologicalOrdering(Graph)
#         List ← empty list
#         Candidates ←  set of all nodes in Graph with no incoming edges
#         while Candidates is non-empty
#             select an arbitrary node a from Candidates
#             add a to the end of List and remove it from Candidates
#             for each outgoing edge from a to another node b
#                 remove edge (a, b) from Graph
#                 if b has no other incoming edges 
#                     add b to Candidates
#         if Graph has edges that have not been removed
#             return "the input graph is not a DAG"
#         else return List


def topologicalOrdering(graph, listNodes):
    print(graph)
    ordering = []
    candidates = getCandidates(graph, listNodes)

    while bool(candidates):
        print(graph)
        candidate = candidates[0]
     
        ordering.append(candidate)
        print(candidate)
        print(ordering)
        candidates.remove(candidate)
        
        # if len(graph) == 1:
        #     print("True", graph)
        #     ordering.append([*graph.values()][0][0])
        # if len(graph[candidate]) == 1 and not graph[candidate] in candidates:
        #     print("True", graph)
        #     ordering.append(graph[candidate][0])
        for node in graph[candidate]:
            newGraph = deepcopy(graph)
            newGraph.pop(candidate)
            if not node in flatten(newGraph):
                ordering.append(node)


        graph.pop(candidate)
        listNodes = flatten(graph)
        newCandidates = getCandidates(graph, listNodes)
        candidates = list(set(candidates+newCandidates))
    return ordering

             
def getCandidates(graph, listNodes):
    candidates = []
    incoming = 0
    for nodeB in listNodes:
        for _, outgoing in graph.items():
            if nodeB in outgoing:
                incoming +=1
        if incoming == 0:
            candidates.append(nodeB)
        else:
            incoming = 0
    return candidates


def readAdjacencyList(strings):
    graph = {}
    for string in strings:
        spplit = string.split(' -> ')
        key = int(spplit[0])
        value = [int(i) for i in spplit[1].split(',')]
        graph[key] = value
    return graph

def flatten(graph):
    nodes = set()
    for node, outgoing in graph.items():
        nodes.add(node)
        nodes.update(outgoing)
    
    return nodes

if __name__ == "__main__":
    
    file = open('data/topologicalOrder.txt', 'r')

    strings = [line.rstrip('\n') for line in file]

    graph =  readAdjacencyList(strings)
    listNodes = flatten(graph)

    print(topologicalOrdering(graph, listNodes))
