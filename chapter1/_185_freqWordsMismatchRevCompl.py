import sys
sys.path.append("..")
from lib import spacedPrint

from _122_frequentWords import maxMap
from _131_reverseComplement import reverseComplement
from _184_freqWordsMismatch import neighbors


#finds the most frequent k-mers that appear in a text with at most d mismatches and their reverse complements
def frequentWordsWithMismatchesAndRevCompl(text, k, d):
    freqTable = {}
    patterns = []
    for i in range(len(text) - k+1):
        pattern = text[i:i+k]
        neighborhood = neighbors(pattern, d)
      
        for neighbor in neighborhood:
            if neighbor in freqTable:
                freqTable[neighbor] += 1
            else:
                freqTable[neighbor] = 1
            
            neighbor_rc = reverseComplement(neighbor)
            if neighbor_rc in freqTable:
                freqTable[neighbor_rc] += 1
            else:
                freqTable[neighbor_rc] = 1

    maximum = maxMap(freqTable)
    for key, value in freqTable.items():
        if value == maximum:
            patterns.append(key)
    return patterns

if __name__ == "__main__": 

    spacedPrint(frequentWordsWithMismatchesAndRevCompl("CTAATTTCTCTAATCGCGTTCTTAGTTTTAATTTAATAATTAGTAGAATTTCGAATTAGAATTTTTCGTAGAATTAGTTCGTTAATCTTAGCTAATAATAATTTTTAATCGCGTAGTTCGTAGTAGCGCTTTCGAATCTCTTTCTCGAATCTTAGAATTTCTAATAATCGTTCTCTCTCGAATAATTTTAGCGTAGAATCGCGCTCGTAGTAGTTAATTTCTCT",7,3))

