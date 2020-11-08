
from _331_pathToGenome import pathToGenome
from _351_deBruijnFromPatterns import deBruijn
from _3101_maximalNonBranchingPaths import maximalNonBranchingPaths

def verticalPrint(list_):
    text = ""
    for item in list_:
        text+=str(item)+"\n"
    print(text[:-1]) #remove last additional "\n"
    
def contigs(patterns):
    deBruijnGraph = deBruijn(patterns)
    maxNonBranchPaths = maximalNonBranchingPaths(deBruijnGraph)

    contigs = []
    for path in maxNonBranchPaths:
        contigs.append(pathToGenome(path))
    return contigs


if __name__ == "__main__":

    file = open("data/contigs.txt", 'r')
    patterns = [line.rstrip('\n') for line in file]

    verticalPrint(contigs(patterns))