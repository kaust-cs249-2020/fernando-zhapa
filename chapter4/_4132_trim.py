import sys
import operator

sys.path.append('..')
from _4131_linearScoring import lScore
from lib import spacedPrint
from dictionaries import molecularMassesNoRepeat, molecularMasses

def trim(leaderboard, spectrum, n):
    # Input: A collection of peptides Leaderboard, a collection of integers Spectrum, and an integer N.
    # Output: The N highest-scoring linear peptides on Leaderboard with respect to Spectrum.

    scores = [lScore(peptide, spectrum) for peptide in leaderboard]
    tupleLeaderboard = [tuple(i) for i in leaderboard]
    dictionary = sorted(zip(scores, tupleLeaderboard), reverse=True)

    sortedLeaderboard = [list(x) for _,x in dictionary]
    sortedScores = [x for x,_ in dictionary]
    

    i = n

    tie = True #assume there is tie after position n-1
    while tie and i<len(leaderboard):
        # print(tupleLeaderboard)
        # print(len(sortedScores))
        # print(i)
        # print(sortedScores[n-1])
        if sortedScores[i] < sortedScores[n-1]:
            tie = False
        else:
            i += 1
    return sortedLeaderboard[:i]
    

if __name__ == "__main__":
    
    file = open('data/trim.txt', 'r')
    
    peptides = file.readline().rstrip('\n').split(' ')
    spectrum = [int(i) for i in file.readline().rstrip('\n').split(' ')]
    n = int(file.readline())

    spacedPrint(trim(peptides, spectrum, n, molecularMasses))