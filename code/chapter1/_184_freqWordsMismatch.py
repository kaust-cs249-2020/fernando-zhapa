import sys
sys.path.append("..")
from lib import spacedPrint

from _181_hammingDistance import hammingDistance
from _122_frequentWords import maxMap

#########################################
##### FREQUENT WORDS WITH MISMATCHES ####

#finds all d neighbors of a pattern. A d-neighbor D of a pattern P is a string that contains maximum d mismatches with respect to P
def neighbors(pattern, d):
    #base cases
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ["A","C","G","T"]
    neighborhood = []
    neighborsSuffix = neighbors(pattern[1:],d)
    for suffixPattern in neighborsSuffix:
        if hammingDistance(pattern[1:], suffixPattern) == d:
            neighborhood.append(pattern[0]+suffixPattern)
        else:
            for nucl in ["A","C","G","T"]:
                neighborhood.append(nucl+suffixPattern)
    return neighborhood

# spacedPrint(neighbors("CGTTA",1))


#finds the most frequent k-mers that appear in a text with at most d mismatches
def frequentWordsWithMismatches(text, k, d):
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
    maximum = maxMap(freqTable)
    for key, value in freqTable.items():
        if value == maximum:
            patterns.append(key)
    return patterns

if __name__ == "__main__": 
    spacedPrint(frequentWordsWithMismatches("GGGGCAGGGGGCGTTGTGATAGGGGATACGTGGGGCAGCAGCGTCGTGGGGCAGCAGTGTGGGGGCGTCGTATAGGGGCGTATATGTGGGGGATAGGGGATACGTGGGGCGTCAGGGGGGGGGCAGCAGCAGCGTGGGGATAGGGGCGTCGTCAGATACGTCAGTGTGCAGATATGTGGGGGCAGATAGGGGATACGTGGGGGGGGCGTCAGCGTTGTGATACAGGGGGCGTCAGTGTGGGGGCGTCAGCGTTGTGCGTCAGCGTATACAGCGTATACAGCAGATAGGGGGGGGATACAGCGTCAGCGTATAGGGGATACAGGGGGATACGTATACAGTGTGGGGGTGTGATAGGGGGGGGGGGGGGGG",7,2))
