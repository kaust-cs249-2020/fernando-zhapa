import sys
sys.path.append("..")
from lib import spacedPrint

from _122_frequentWords import frequencyTable

################################################
############## CLUMP FINDING PROBLEM ###########

#finds all distinct k-mers forming (L,t)-clumps in genome. 
#A k-mer forms a (L,t)-clump if it appears at least t times in an interval of lenght L.   
def findClumps(genome, k, l, t):
    patterns = []
    for i in range(len(genome) - l + 1):
        window = genome[i:i+l]
        freqTable = frequencyTable(window,k)

        for pattern, frequency in freqTable.items():
            if frequency >= t and not (pattern in patterns):
                patterns.append(pattern)
    return patterns

if __name__ == "__main__": 
    genome = "ATTTTTACCTTGCATAGGGAGATAAGAAAAGGCAAGAATAAAGGGGCACGATGCACGATATATGATCGATATCACGCTGTTTATCCTCGCCTAACTAAACCCCTCAGGCGCGGTGTTTGTTCACATTTGACGTGTGTCAGACCCTCACAAATGTACTTGGCTTATGGCTTATGGCTTATTGGCTTATTGGGACCAGTTTAGACACGCCTTCGCACTCCCAGTAACTACTGGTAGCGAAGGCAACCGCCCCGAACTGCGTCCTCCATAGTAGTATAGCGGAACCCATAACTGTCGTACCTACACAACGGTGCCAAGGGATCACCGTAGCCTGCCGAACCGGGTATATATGGGTCATGTATGTGAGCTACCCATTTGAACTCTTCTTTGGGTAACCGTGGCCGTCTTAGTTGGGCTGACTTTTCATATGACTCATAGTGATTGCACGTTTAGCGTGTTGGGGATAGATCCGGTAATGACCTCCAATGCTTAGTTGATCTCGCACATTTGGTTGCCTATGTAATGTGTTTCCCGACCGAACCGTGGCAATAACTTAGGGTCAAATGGAGACGACATTCCACGATCATGGTCATGCGCAGAGGTCGATAACGAACTGGACGAGGGTAGCGCAACCCACGTCCTCGCAATGGCAAGTACGATGCCGCGAAAACATGGGGCCAATCATGCATCTCGTCGATGGGCAGCGGCAGAGGGGGTCCTCTTTCTTAGGTTGTTCGGTCGGGGACTATGGTGCCTAGGACATCACATAAAAGTAAAGTAGCTGTTCCTGTCCCCCCGCGGTGCGGTCCCCCCGCGGTTTATGAATTTTTCAACCCCGAGTTGTACGTCCGTTAAGGAGCTGGCATCTTAGTGGGTTCAGAAACCGCCGTGTTTTTTCCGTGTTTGTTTCGCCTCGGTCGGTCCCGCGTGCACTGTGCGAGTGGATTTGCCATACAGAATTTTAGGTAGTCTCTATCATTATCTATCATCGTCGCGTGAATGGAAGCCCATGTTCCGTGGAATCGAGTTAGTTGGGATCGTGAGTAGCTGCTATCCCGAAAGACTATCTCTCACCGCCGCGTGAAGTTGCGAAGGCGCCCATGTCAGTAGCCGCAAAGAGAAACTAACAGTGTTTCCCCTTCTATGCGTACGTCCGAATCGGGCGGGATATGTGAACTCTAACACGATATTACCAGGGAGAGGCGATATCCTTATTCACTCGCGGGAGAAACACGTTACCGAGACCCCTAACCTGCGGAGTGCCTCCCTGGGCAGCCGAAATGGAGTCGTAAACCCGAACGTATTTGGGCATACTCGGTACCTTCGAAACGACGGGACGGAAACGACGGAAAAACTGGGGTTTCGAACCATCCGTCAACGATTCGGTCACACATCTCTAGGGCGCGGGAAGACATCATTTATGAGTATCGTAAGAAGCTAGAAGCTAGTAAAGCTAGTGTACAATTGGCTGTTGGTATTTTTCGCGCCCGTTGATACATGCGTCTTCCAGTGACGTGGTGAACCATTGTCTCGCAACTTCATGAGAAACCAGGTTTAAACGGGGATGCGTTTAATGCAATCCATGCTTTTTCTCGATGGGCACTCATAGGTGCGATCTTACTGAACATCTCGATTCCATTCCATGGATGTTCCATGGACGATTTTAGGGATGATGGGCCGCCGCCTCCGACCGACGCTCTGAGCTCGCTAATTGGTTCCCATCGATCGTTAGACACTCAATCTCATCTAAGCCTGAATGCTCCTATGTCAGATGGATGTATGTTTTTCGTCGTTCGATCGTTCGATCGTTCGATCGTTCGATCGTTCGATCGTTCGATCGTTCGATCGTTCGACGGACTCCCGGACTCCCGGACTCCCGGACTCCCGCGGACTCCGACCGGACTCC"
    spacedPrint(findClumps(genome, 8, 25, 4))


    ## EXERCISE BREAK
    file = open("data/E_coli.txt", 'r')
    text_ec = file.read()
    print(len(findClumps(text_ec,9,500,3)))
