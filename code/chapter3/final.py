from _392_stringSpelledByGappedPatterns import readGappedSequence
from _393_reconstructionFromReadPairs import reconstructionFromReadPairs, deBruijn
from lib import verticalPrint, printGraphAdjList

file = open("../../data/reads.txt", 'r')

pairsStr = [line.rstrip('\n') for line in file]

pairs = readGappedSequence(pairsStr)

deBruijnGraph = deBruijn(pairs)


printGraphAdjList(deBruijnGraph)

print(reconstructionFromReadPairs(120,1000,pairs))