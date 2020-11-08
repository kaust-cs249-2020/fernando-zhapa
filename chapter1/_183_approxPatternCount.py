from _181_hammingDistance import hammingDistance

#counts the number of approximate occurrences of a pattern in a text with hamming distance less or equeal than an integer d 
def approximatePatternCount(d, pattern, text):
    patternLength = len(pattern)
    count = 0
    for i in range(len(text) - patternLength +1):
        if hammingDistance(pattern, text[i:i+patternLength]) <= d:
            count+=1
    return count

if __name__ == "__main__": 
    print(approximatePatternCount(2,"GGCTGAG", "TCTTGTTCTTCACAATATTCAAACGAAGATGTTAATTAAAGTTGGTTACCCATAATCACCGTACGGGGCATCCCGAAGCGTAACAATGGTGAATGTCGATCTGGTGGCAAGTGGCGTACCAACGTTCGCTGAGTAATTCGGTGGGCTGAGTCGGCCATTATGACCATCCCGTGGTTAGCGGGAGTGTGCCCCTTGCGAAGTGCTCCGTCGTGGGCCATTCGAAAAGCCACGTCCTCCGATGATTCAGAGAACAGGGTATCTGGGACAATTAGTGGTGACTAACACTGCATCGCAAGAACTCAGATAAAAATTCGAACACGCTGTGGTGGTCC"))

