import sys
sys.path.append("..")

from dictionaries import geneticCode
from lib import verticalPrint
from chapter1._131_reverseComplement import reverseComplement
from _421_proteinTranslation import proteinTranslation

def transcription(dna):
    rna = ""
    for nucl in dna:
        if nucl == 'T':
            rna += 'U'
        else:
            rna += nucl
    return rna

def peptideEncoding(dna, peptide, geneticCode):
    # Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
    # Output: All substrings of Text encoding Peptide (if any such substrings exist).
    
    patterns = []

    lenPattern = 3 * len(peptide)

    for i in range(len(dna)-lenPattern +1):
        pattern = dna[i:i+lenPattern]
        revComplPattern = reverseComplement(pattern)

        if proteinTranslation(transcription(pattern), geneticCode) == peptide:
            patterns.append(pattern)
        elif proteinTranslation(transcription(revComplPattern), geneticCode) == peptide:
            patterns.append(pattern)
        
    return patterns


if __name__ == "__main__":
    
    file = open('data/peptideEncoding.txt')

    dna = file.readline().rstrip('\n')
    peptide = file.readline().rstrip('\n')

    verticalPrint(peptideEncoding(dna, peptide, geneticCode))

    
