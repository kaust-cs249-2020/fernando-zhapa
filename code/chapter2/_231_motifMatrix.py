import sys
sys.path.append("..")
from lib import printDict, col
from math import log2


# given a set of motifs represent as a matrix, returns the count of nucleotides for each column of the matrix
def countMotifs(motifs):
    k = len(motifs[0])
    count = {'A': [0]*k, 'C': [0]*k, 'G': [0]*k, 'T': [0]*k}

    for j in range(k):
        for i in range(len(motifs)):
            nucleotide = motifs[i][j]
            count[nucleotide][j] += 1
    return count

def profileMotifs(motifs):
    n = len(motifs)
    k = len(motifs[0])
    count = {'A': [0]*k, 'C': [0]*k, 'G': [0]*k, 'T': [0]*k}

    for j in range(k):
        for i in range(len(motifs)):
            nucleotide = motifs[i][j]
            count[nucleotide][j] += 1/n
    return count

def entropyOfColumn(column):
    entropy = 0
    for i in range(len(column)):
        val = column[i]
        if val != 0:
            entropy += val*log2(val)
    return -entropy

def entropyOfMatrix(matrix):
    profile = profileMotifs(matrix)
    matrix = []
    for key, value in profile.items():
        matrix.append(value)

    entropy = 0
    for j in range(len(matrix[0])):
        entropy += entropyOfColumn(col(matrix,j))
    return entropy

matrix = [
    "TCGGGGGTTTTT",
    "CCGGTGACTTAC",
    "ACGGGGATTTTC",
    "TTGGGGACTTTT",
    "AAGGGGACTTCC",
    "TTGGGGACTTCC",
    "TCGGGGATTCAT",
    "TCGGGGATTCCT",
    "TAGGGGAACTAC",
    "TCGGGTATAACC"
]

print(entropyOfMatrix(matrix))