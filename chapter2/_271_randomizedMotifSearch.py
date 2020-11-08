import sys
sys.path.append("..")

from random import randint
from _231_motifMatrix import profileMotifs, score, consensus
from _251_profileMostProbableKmer import profileMostProbableKmer
from lib import verticalPrint

def randomMotifs(strings, k, t):
    #makes randomly choice of t k-mers, one from each dna string
    upperBound = len(strings[0]) - k
    motifs = []
    for i in range(t):
        randIndex = randint(0,upperBound)
        motifs.append(strings[i][randIndex:randIndex+k])
    return motifs


def motifs(profile,dna):
    #returns the most probable k-mer in each dna string
    k = len(profile[0])
    motifs = [profileMostProbableKmer(row,k,profile) for row in dna]
    return motifs

def randomizedMotifSearch(dna, k, t):
    bestMotifs = randomMotifs(dna, k, t)
    while True:
        profile = profileMotifs(bestMotifs)
        newMotifs = motifs(profile,dna)
        if score(newMotifs) < score(bestMotifs):
            bestMotifs = newMotifs
        else:
            return bestMotifs


def wrapperRMS(dna,k,t, iter):
    motifs = randomizedMotifSearch(dna,k,t)
    for i in range(iter-1):
        newMotifs = randomizedMotifSearch(dna,k,t)
        if score(newMotifs) < score(motifs):
            motifs = newMotifs
    return motifs








if __name__ == "__main__": 
    file = open("data/subtle_motif_dataset.txt", 'r')
    dna = [line.rstrip('\n') for line in file]

    result_motifs = wrapperRMS(dna, 15, 10,1000)
    score_motifs = score(result_motifs)
    consensusMotifs = consensus(result_motifs)
    verticalPrint(result_motifs)
    print(score_motifs)
    print(consensusMotifs)