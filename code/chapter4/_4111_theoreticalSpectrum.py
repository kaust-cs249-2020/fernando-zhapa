import sys
sys.path.append('..')

import os

from lib import spacedPrint
from dictionaries import molecularMasses

def linearSpectrum(peptide): #peptide is a list of integer masses
    prefixMass = [0]
    
    for i in range(len(peptide)):      
        mass = peptide[i]
        prefixMass.append(prefixMass[i] + mass)
    linearSpectrum = [0]

    for i in range(len(prefixMass) - 1):
        for j in range(i+1,len(prefixMass)):
            linearSpectrum.append(prefixMass[j] - prefixMass[i])
        
    linearSpectrum.sort()
    return linearSpectrum

def cyclicSpectrum(peptide):
    prefixMass = [0]

    for i in range(len(peptide)):
        mass = peptide[i]
        prefixMass.append(prefixMass[i] + mass)

    peptideMass = prefixMass[-1]
    cyclicSpectrum = [0]
    for i in range(len(prefixMass) - 1):
        for j in range(i+1,len(prefixMass)):
            massSubPeptide = prefixMass[j] - prefixMass[i]
            cyclicSpectrum.append(massSubPeptide)
            
            if i > 0 and j < len(peptide):
                cyclicSpectrum.append(peptideMass - massSubPeptide)
    cyclicSpectrum.sort()
    return cyclicSpectrum

if __name__ == "__main__":
    
    file = open("data/linearSpectrum.txt", 'r')

    peptide = file.readline()

    spacedPrint(linearSpectrum(peptide, molecularMasses, mode="amino"))