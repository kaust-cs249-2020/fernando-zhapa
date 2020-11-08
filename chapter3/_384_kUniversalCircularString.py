import sys
sys.path.append('../chapter1')

from _181_hammingDistance import hammingDistance
from _351_deBruijnFromPatterns import deBruijn
from _381_eulerianCycle import eulerianCycle
from _331_pathToGenome import pathToGenome

def neighbors(pattern, d):
    #base cases
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ["0","1"]
    neighborhood = []
    neighborsSuffix = neighbors(pattern[1:],d)
    for suffixPattern in neighborsSuffix:
        if hammingDistance(pattern[1:], suffixPattern) == d:
            neighborhood.append(pattern[0]+suffixPattern)
        else:
            for char in ["0","1"]:
                neighborhood.append(char+suffixPattern)
    return neighborhood


def kUniversalCircularString(k):

    strings = neighbors("0"*k,k)
    deBruijnGraph = deBruijn(strings)
    cycle = eulerianCycle(deBruijnGraph)
    string = pathToGenome(cycle)[:-k+1]
    return string

if __name__ == "__main__":
    
    print(kUniversalCircularString(5))