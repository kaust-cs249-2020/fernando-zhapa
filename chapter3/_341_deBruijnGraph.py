import sys
sys.path.append("..")

from lib import printGraphAdjList


def overlap(patterns):
    # Input: A collection Patterns of k-mers.
    # Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. (You may return the nodes and their edges in any order.)

    graph = {}
    for i in range(len(patterns)-1):
        if patterns[i] in graph:
            graph[patterns[i]].append(patterns[i+1])
        else:
            graph[patterns[i]] = [patterns[i+1]]
    return graph


def deBruijnGraph(k, text):
    # Input: An integer k and a string Text.
    # Output: DeBruijn_k(Text).
    patterns = []
    for i in range(len(text) - (k-1) + 1):
        patterns.append(text[i:i+(k-1)])
    adajacencyList = overlap(patterns)
    return adajacencyList


if __name__ == "__main__":

       
    file = open("data/deBrujin.txt", 'r')
    k = int(file.readline())
    text = file.readline()[:-1]

    text = "TAATGCCATGGGATGTT"
    printGraphAdjList(deBruijnGraph(2,text))
    print("\n")
    printGraphAdjList(deBruijnGraph(3,text))
    print("\n")
    printGraphAdjList(deBruijnGraph(4,text))

    text2 = "TAATGCCATGGGATGTT"
    text3 = "TAATGGGATGCCATGTT"
    print("\n")
    printGraphAdjList(deBruijnGraph(3,text2))
    print("\n")
    printGraphAdjList(deBruijnGraph(3,text3))
    print("\n")
    

    
