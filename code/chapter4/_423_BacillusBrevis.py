import sys
sys.path.append('..')

from lib import verticalPrint
from dictionaries import geneticCode
from _422_peptideEncoding import peptideEncoding


if __name__ == "__main__":
    
    file = open("data/Bacillus_brevis.txt")

    dna = ''.join([line.rstrip('\n') for line in file])
  
    peptide = "VKLFPWFNGY"

    verticalPrint(peptideEncoding(dna, peptide, geneticCode))