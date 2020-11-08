import sys
sys.path.append("..")

from lib import printGraphAdjList

def deBruijn(patterns):
    # Input: A collection of k-mers Patterns.
    # Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
    adjacencyList = {}
    for pattern in patterns:
        preffix = pattern[:-1]
        suffix = pattern[1:]
        if not preffix in adjacencyList:
            adjacencyList[preffix] = [suffix]
        else:
            adjacencyList[preffix].append(suffix)
    return adjacencyList

if __name__ == "__main__":
    

    # patterns = [
    #     "GAGG",
    #     "CAGG",
    #     "GGGG",
    #     "GGGA",
    #     "CAGG",
    #     "AGGG",
    #     "GGAG",
    # ]

       
    file = open("data/deBrujinFromPatterns.txt", 'r')
    patterns = [line.rstrip('\n') for line in file]


    printGraphAdjList(deBruijn(patterns))