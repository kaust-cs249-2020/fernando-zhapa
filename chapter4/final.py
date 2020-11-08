
import sys
sys.path.append('..')

from lib import toStr
from _492_convolutionCyclopeptideSequencing import convolutionCyclopeptideSequencing
from math import floor
from _4111_theoreticalSpectrum import cyclicSpectrum

def removeCharge(spectrum):
    return [i-1 for i in spectrum]



def sequence(m,n,spectrum):
    spectrum = removeCharge(spectrum)
    peptide = convolutionCyclopeptideSequencing(m,n,spectrum)
    return peptide

if __name__ == "__main__":
    
    file = open("data/final.txt", 'r')

    m = int(file.readline())
    n = int(file.readline())


    spectrum = [floor(float(i)) for i in file.readline().rstrip('\n').split(' ')]
    peptide = sequence(m,n,spectrum)
    print(toStr(peptide))
