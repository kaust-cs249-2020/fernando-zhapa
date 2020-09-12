import sys
sys.path.append("..")
from lib import spacedPrint

###################################
######### FREQUENT WORDS ##########

#builds a frequency table of the patterns of length k occuring in a string
def frequencyTable(text, k):
    freqTable = {}
    for i in range (len(text) - k + 1):
        currPattern = text[i:i+k]
        if currPattern in freqTable:
            freqTable[currPattern] += 1
        else:
            freqTable[currPattern] = 1
    return freqTable
#print(frequencyTable("ACGTTTCACGTTTTACGG", 3))

#finds the maxValue in a dictionary representing a frequency table
def maxMap(dictionary):
    maximum = float('-inf')
    for value in dictionary.values():
        if value > maximum:
            maximum = value
    return maximum
# print(maxMap(frequencyTable("ACGTTTCACGTTTTACGG", 3)))

#finds the most occuring patterns of length k in a string
def frequentWords(text, k):
    freqTable = frequencyTable(text, k)
    maximum = maxMap(freqTable)
    patterns = []
    for pattern, frequency in freqTable.items():
        if freqTable[pattern] == maximum:
            patterns.append(pattern)
    return patterns

# text_fw = "TCTGGCCAATTATAACGGTCTGGCCAACGTCTGGGTTCTGGCCAACTAACATCGTCTGGGTTCTGGCCAATCTGGCCAATCTGGCCAACTAACATTCTGGCCAATCTGGCCAACTAACATTTATAACGGAACCAGGCTTATAACGGCTAACATTCTGGCCAAAACCAGGCAACCAGGCTTATAACGGCTAACATCGTCTGGGTCTAACATCGTCTGGGTTTATAACGGTTATAACGGAACCAGGCCTAACATTTATAACGGTTATAACGGCGTCTGGGTTTATAACGGCGTCTGGGTTCTGGCCAACTAACATTTATAACGGTTATAACGGAACCAGGCCGTCTGGGTTTATAACGGTTATAACGGTCTGGCCAACGTCTGGGTTTATAACGGAACCAGGCCTAACATAACCAGGCAACCAGGCTCTGGCCAACTAACATTTATAACGGCGTCTGGGTTTATAACGGCGTCTGGGTTCTGGCCAATTATAACGGTTATAACGGAACCAGGCAACCAGGCCTAACATTTATAACGGAACCAGGCTTATAACGGTCTGGCCAATTATAACGGCTAACATTTATAACGGCGTCTGGGTCTAACATCGTCTGGGTCTAACATCTAACATTTATAACGGCGTCTGGGTCTAACATTTATAACGGTCTGGCCAATCTGGCCAATTATAACGGTTATAACGGAACCAGGCAACCAGGCTTATAACGGTTATAACGGTTATAACGGAACCAGGCCGTCTGGGTTTATAACGGTTATAACGGTCTGGCCAATTATAACGGCTAACATCGTCTGGGTAACCAGGCCTAACATCGTCTGGGTCGTCTGGGTTCTGGCCAACGTCTGGGTCGTCTGGGTCGTCTGGGT"
# spacedPrint(frequentWords(text_fw, 13))
