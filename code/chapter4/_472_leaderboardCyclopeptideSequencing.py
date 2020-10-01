import sys
sys.path.append('..')

import os

from lib import toStr, verticalPrint
from _461_cyclopeptide_Sequencing import mass, parentMass
from _471_cyclicScoring import cScore
from _4131_linearScoring import lScore
from _4132_trim import trim
from dictionaries import molecularMassesExtended, molecularMassesNoRepeat

def expand(peptides, dictionary):
    expanded = []
    for peptide in peptides:
        for _, value in dictionary.items():
            expanded.append(peptide + [value])
    return expanded



def leaderboardCyclopeptideSequencing(spectrum, n, dictionary):

    # Input: An integer N and a collection of integers Spectrum.
    # Output: LeaderPeptide after running LeaderboardCyclopeptideSequencing(Spectrum, N).

    leaderboard = [[]]
    leaderPeptide = []
    while bool(leaderboard):
        leaderboard =  expand(leaderboard, dictionary)        
        for peptide in leaderboard[:]:
            if mass(peptide) == parentMass(spectrum):
                if cScore(peptide, spectrum) > cScore(leaderPeptide, spectrum):
                    leaderPeptide = peptide
            elif mass(peptide) > parentMass(spectrum):
                leaderboard.remove(peptide)
        leaderboard = trim(leaderboard, spectrum, n)
    
    return leaderPeptide
    

def leaderboardCyclopeptideSequencingAll(spectrum, n, dictionary):

    # Input: An integer N and a collection of integers Spectrum.
    # Output: LeaderPeptide after running LeaderboardCyclopeptideSequencing(Spectrum, N).

    leaderboard = [[]]
    leaderPeptides = [[]]
    while bool(leaderboard):
        leaderboard =  expand(leaderboard, dictionary)   
        for peptide in leaderboard[:]:
            if mass(peptide) == parentMass(spectrum):
                if cScore(peptide, spectrum) > cScore(leaderPeptides[0], spectrum):
                    leaderPeptides = [peptide]
                elif cScore(peptide, spectrum) == cScore(leaderPeptides[0], spectrum):
                    if not peptide in leaderPeptides:
                        leaderPeptides.append(peptide)
            elif mass(peptide) > parentMass(spectrum):
                leaderboard.remove(peptide)
        leaderboard = trim(leaderboard, spectrum, n)
    
    print("Total peptides: " + str(len(leaderPeptides)))

    return leaderPeptides



if __name__ == "__main__":
    
    if  __debug__:
        file = open(os.getcwd() + '/code/chapter4/data/leaderboard.txt')
    else:
        file = open('data/leaderboard.txt')

    n = int(file.readline())
    spectrum = [int(i) for i in file.readline().rstrip('\n').split(' ')]
    # print(n)
    # print(spectrum)
    result = leaderboardCyclopeptideSequencingAll(spectrum, n, molecularMassesNoRepeat)
    #print(toStr(result))
    verticalPrint([toStr(i) for i in result])

