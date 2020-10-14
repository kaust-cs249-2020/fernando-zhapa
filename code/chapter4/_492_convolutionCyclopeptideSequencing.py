import sys
sys.path.append('..')

from itertools import groupby 
from lib import toStr, spacedPrint
from dictionaries import molecularMassesExtended
from _491_spectralConvolution import spectralConvolution
from _4131_linearScoring import lScore
from _471_cyclicScoring import cScore
from _472_leaderboardCyclopeptideSequencing import leaderboardCyclopeptideSequencing, leaderboardCyclopeptideSequencingAll

def trimConvolution(m, spectralConv):
    spectralConv.sort(reverse=True)
    start = 0

    lenSpecConv = len(spectralConv)
    end = lenSpecConv - 1

    tie = True

    ### Find masses between 200 - 57
    foundStart = False
    foundEnd = False
    while start <= end and (not foundStart or not foundEnd):
        if spectralConv[start] > 200:
            start += 1
        else:
            foundStart = True
        if spectralConv[end] < 57:
            end -= 1
            foundEnd = True

    spectralConv = spectralConv[start:end+1]
    ####

    ### Group similar masses and sort by occurence
    groups = [list(y) for x, y in groupby(spectralConv)] 
    sortedGroups = sorted(groups, key=len, reverse=True)
    ###

    ### Take the m most frequent with ties
    i = m
    tie = True
    while tie and i<len(sortedGroups):
        if len(sortedGroups[i]) < len(sortedGroups[m-1]):
            tie = False
        else:
            i += 1
    
    freqs = []
    for j in range(i):
        freqs.append(sortedGroups[j][0])

    return freqs


def convolutionCyclopeptideSequencing(m, n, spectrum):

    # Input: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.
    # Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the convolution of Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).

    spectrum.sort()
    spectralConv = spectralConvolution(spectrum)

    mostFreq = trimConvolution(m, spectralConv)

    dictionary = {}
    for i in range(len(mostFreq)):
        dictionary[i] = mostFreq[i]


    sequencedPeptide = leaderboardCyclopeptideSequencing(spectrum,n,dictionary)

    return sequencedPeptide


def convolutionCyclopeptideSequencingAll(m, n, spectrum):

    # Input: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.
    # Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the convolution of Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).

    spectrum.sort()
    spectralConv = spectralConvolution(spectrum)

    mostFreq = trimConvolution(m, spectralConv)

    dictionary = {}
    for i in range(len(mostFreq)):
        dictionary[i] = mostFreq[i]


    sequencedPeptides = leaderboardCyclopeptideSequencingAll(spectrum,n,dictionary)
    print("Total peptides: " + str(len(sequencedPeptides)))
    print("Score: " + str(cScore(sequencedPeptides[0], spectrum)))
    return sequencedPeptides



if __name__ == "__main__":
    file = open("data/convSeq_Spec25.txt", 'r')

    m = int(file.readline())
    n = int(file.readline())


    spectrum = [int(i) for i in file.readline().rstrip('\n').split(' ')]

#    print(toStr(convolutionCyclopeptideSequencingAll(m,n,spectrum)))
    peptides = convolutionCyclopeptideSequencingAll(m,n,spectrum)
    peptidesStr = [toStr(i) for i in peptides]
    spacedPrint(peptidesStr)

