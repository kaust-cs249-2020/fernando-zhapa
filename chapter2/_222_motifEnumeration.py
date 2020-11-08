import sys
sys.path.append("../chapter1")
sys.path.append("..")

from lib import spacedPrint
from _181_hammingDistance import hammingDistance
from _184_freqWordsMismatch import neighbors

# checks whether a pattern is a substring of another string with at most d mismatches
def isSubstringWithMismatches(pattern, string, d):
    k = len(pattern)
    for i in range(len(string) - k + 1):
        substring = string[i:i+k]
        if hammingDistance(pattern, substring) <= d:
            return True
    return False


# Given a collection of strings Dna and an integer d, returns all (k,d)-motifs.
# A k-mer is a  if it appears in every string from Dna with at most d mismatches.
def motifEnumeration(strings, k, d):
    patterns = []
    for i in range(len(strings[0]) - k +1):
        pattern = strings[0][i:i+k]
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            count = 0
            for string in strings:
                if isSubstringWithMismatches(neighbor, string, d):
                    count+=1
                else:
                    break
            if count == len(strings):
                patterns.append(neighbor)
    patterns = list(dict.fromkeys(patterns))
    return patterns
            
if __name__ == "__main__": 
    spacedPrint(motifEnumeration(["AAGTAGTACGGATGCCACGTTTGCC",
    "GTTGCGGTGAGCAAGCAGTACCTAA",
    "TAGTATCCGCTAATCTCGACTCAAT",
    "CAGGGTATGCCGATAGAGCTGAGTA",
    "CATTATGGATCTACCCCTCGCAATT",
    "TCATACATGATGGGGAACTACATAC"], 5, 2))
