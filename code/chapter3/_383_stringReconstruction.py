from _351_deBruijnFromPatterns import deBruijn
from _382_eulerianPath import eulerianPath
from _331_pathToGenome import pathToGenome

def stringReconstruction(patterns):

    # Input: An integer k followed by a list of k-mers Patterns.
    # Output: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)

    deBruijnGraph = deBruijn(patterns)
    eulerPath = eulerianPath(deBruijnGraph)
    text = pathToGenome(eulerPath)
    return text


if __name__ == "__main__":
    
    file = open("/home/ferynando7/KAUST/Fall2020/CS249/fernando-zhapa/data/stringRecons.txt", 'r')
    patterns = [line.rstrip('\n') for line in file]


    # patterns = [
    #     "CTTA",
    #     "ACCA",
    #     "TACC",
    #     "GGCT",
    #     "GCTT",
    #     "TTAC",
    # ]

    print(stringReconstruction(patterns))