from _382_eulerianPath import eulerianPath
from _392_stringSpelledByGappedPatterns import stringSpelledByGappedPatterns, readGappedSequence

def deBruijn(gappedPatterns):
    # Input: A collection of k-mers Patterns.
    # Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
    adjacencyList = {}
    for pattern in gappedPatterns:
        initial = pattern[0]
        terminal = pattern[1]
        prefix = (initial[:-1],terminal[:-1])
        suffix = (initial[1:],terminal[1:])
        if not prefix in adjacencyList:
            adjacencyList[prefix] = [suffix]
        else:
            adjacencyList[prefix].append(suffix)
    return adjacencyList

def reconstructionFromReadPairs(k, d, pairs):
    deBruijnGraph = deBruijn(pairs)
    path = eulerianPath(deBruijnGraph)
    return stringSpelledByGappedPatterns(k, d, path)

if __name__ == "__main__":
    
    file = open("/home/ferynando7/KAUST/Fall2020/CS249/fernando-zhapa/data/pairs.txt", 'r')
    pairsStr = [line.rstrip('\n') for line in file]
    pairs = readGappedSequence(pairsStr)


  
    print(reconstructionFromReadPairs(50,200,pairs))


