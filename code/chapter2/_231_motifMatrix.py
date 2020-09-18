import sys
sys.path.append("..")
from lib import printDict, col
from math import log2


def countMotifs(motifs):
# given a set of motifs represent as a matrix, returns the count of nucleotides for each column of the matrix
    k = len(motifs[0])
    count = {'A': [0]*k, 'C': [0]*k, 'G': [0]*k, 'T': [0]*k}

    for j in range(k):
        for i in range(len(motifs)):
            nucleotide = motifs[i][j]
            count[nucleotide][j] += 1
    return count

def score(motifs):
# computes the score of the whole motif matrix by counting, for each column, the unpopular letters
    count = [*countMotifs(motifs).values()]
    score = 0
    for j in range(len(count[0])):
        column = [row[j] for row in count]
        score += (sum(column)-max(column))
    return score

def consensus(motifs):
    nucl = {0:'A', 1:'C', 2:'G', 3:'T'}
    count = [*countMotifs(motifs).values()]
    kmer = ""
    for j in range(len(count[0])):
        col = [row[j] for row in count]
        kmer += nucl[col.index(max(col))]
    return kmer



def profileMotifsNoSucc(motifs):
    #computes profile matrix without applying succession rule
    n = len(motifs)
    k = len(motifs[0])
    count = {'A': [0]*k, 'C': [0]*k, 'G': [0]*k, 'T': [0]*k}

    for j in range(k):
        for i in range(len(motifs)):
            nucleotide = motifs[i][j]
            count[nucleotide][j] += 1/n
    return [*count.values()]

def profileMotifs(motifs):
    n = len(motifs)
    k = len(motifs[0])
    count = {'A': [1]*k, 'C': [1]*k, 'G': [1]*k, 'T': [1]*k}

    for j in range(k):
        for i in range(len(motifs)):
            nucleotide = motifs[i][j]
            count[nucleotide][j] += 1/n
    return [*count.values()]

def entropyOfColumn(column):
    entropy = 0
    for i in range(len(column)):
        val = column[i]
        if val != 0:
            entropy += val*log2(val)
    return -entropy

def entropyOfMatrix(matrix):
    profile = profileMotifsNoSucc(matrix)

    entropy = 0
    for j in range(len(profile[0])):
        entropy += entropyOfColumn(col(profile,j))
    return entropy


if __name__ == "__main__": 
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