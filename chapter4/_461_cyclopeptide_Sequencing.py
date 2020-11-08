import os
import sys
sys.path.append('..')

from lib import toStr, spacedPrint
from copy import deepcopy
from dictionaries import molecularMassesNoRepeat, molecularMasses
from _4111_theoreticalSpectrum import cyclicSpectrum, linearSpectrum


def mass(peptide):
    return sum(peptide)

def parentMass(spectrum):
    return spectrum[-1]


def consistent(peptide, spectrum):
    isConsistent = True
    accSpec = 0
    accPep = 0

    while accSpec < len(spectrum) and accPep < len(peptide) and isConsistent:

        if peptide[accPep] == spectrum[accSpec]:
            accSpec += 1
            accPep += 1
        elif peptide[accPep] < spectrum[accSpec]:
            isConsistent = False
        else:
            accSpec +=1
    if accSpec == len(spectrum) and accPep < len(peptide):
        isConsistent = False
    return isConsistent



def cyclopeptideSequencing(spectrum, peptide = []):
    finalPeptides = []
    for _, value in molecularMassesNoRepeat.items():
        newPeptide = peptide + [value]
        peptideSpecCyclic =  cyclicSpectrum(peptide + [value],molecularMasses,"mass")
        peptideSpecLinear = linearSpectrum(peptide + [value], molecularMasses, "mass")
        if parentMass(spectrum) == mass(newPeptide, "mass"):
            if peptideSpecCyclic == spectrum:
                finalPeptides.append(newPeptide)
        elif consistent(peptideSpecLinear, spectrum):
            finalPeptides = finalPeptides + cyclopeptideSequencing(spectrum, newPeptide)
    return finalPeptides



# def cyclopeptideSequencing(spectrum):
#     candidatePeptides = []
#     finalPeptides = []

if __name__ == "__main__":
    
    if __debug__:
        file = open(os.getcwd() + '/code/chapter4/data/sequencing.txt', 'r')
    else:
        file = open('data/sequencing.txt', 'r')

    spectrum = [ int(i) for i in file.readline().split(' ')]
    cycloPeptides = cyclopeptideSequencing(spectrum)
    cycloPeptidesStr = [toStr(i) for i in cycloPeptides]
    spacedPrint(cycloPeptidesStr)