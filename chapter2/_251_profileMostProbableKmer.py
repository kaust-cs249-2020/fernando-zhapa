from _231_motifMatrix import profileMotifsNoSucc
def profileProbability(string, profileMatrix):
    #computes the profile-probability of a string
    
    nucl = {'A':0, 'C':1, 'G':2, 'T':3} #to access the profile matrix easily
    if len(string) != len(profileMatrix[0]):
        return -1
    prob = 1
    for i in range(len(string)):
        currNucl = string[i]
        prob *= profileMatrix[nucl[currNucl]][i]
    return prob


def profileMostProbableKmer(text, k, profileMatrix):
    #computes the profile-most probable k-mer in a text 
    prob = float('-inf')
    mostProbable = ""
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        kmerProb = profileProbability(kmer, profileMatrix)
        print(kmer,kmerProb)
        if kmerProb > prob:
           
            prob = kmerProb
            mostProbable = kmer
    return mostProbable


if __name__ == "__main__": 
    profileMatrix = [
        [0.258, 0.242, 0.303, 0.242, 0.318, 0.333, 0.273, 0.242, 0.242, 0.273, 0.227, 0.258, 0.288, 0.212, 0.273],
        [0.258, 0.227, 0.288, 0.242, 0.182, 0.258, 0.273, 0.197, 0.227, 0.182, 0.288, 0.242, 0.348, 0.318, 0.212],
        [0.273, 0.227, 0.136, 0.212, 0.273, 0.212, 0.167, 0.273, 0.212, 0.318, 0.227, 0.197, 0.167, 0.212, 0.303],
        [0.212, 0.303, 0.273, 0.303, 0.227, 0.197, 0.288, 0.288, 0.318, 0.227, 0.258, 0.303, 0.197, 0.258, 0.212]
    ]

    matrix2 = [
        "ACTG",
        "AGTC",
        "GCTG",
        "ACGT",
        "AGCA",
        "CCAG",
        "TGTC",
        "GATG",
        "ATGT",
        "AGAA",
    ]

    kmer = "TAGA"

    # print(profileMostProbableKmer("GAGGGTGGCTGGCCATGGCGTTCTTGATTATTCGTGGCGCGCGGAAAACTCATTCCATGGCCATCATAAGCAATCGGAGGAAGTTTTTTTGAGCTAGCTTCTCACGAGAACGCAGGTTTCTGGGGTGTTATCCCAATACGGCAAGGGGATAAGATTCAGATAGGAGTAATCCATGACATGGCAACCACACTTACGCATTCCCTCGCTTAAATTAGACAGGAAAGTTGCACGACGCGTACCGGACTTACGTCAAGTAGAGTGCGGCTTGTGCATTCTAGGCGTCCATTGATCTTTAAGTCGCGAGTAGTGCATAAGTTTAGCCTGGTCTGCCGCCAAGGCGCGCGCTGTTCGGCCGAGAACTAGATGGCTGAAATGTCTAATGCAACAGAATACACAATATAGCCCCATAGCCCCTGCCGGCTAGGTCTGGGACCAAACGCAGAGGAAGAACGAGTGTATTAGACTACTAAACCGGGCATGAGTAGAGCCGCCTGTTCGATTCCTCCTCAAACGGACTACACCATACATATTCTTTATGCCATCTGGATATGGACCTGTGTAATAGCCATCACGCGCGGCGGATGTCCAGAATCCAGCGCGGGGTGTTGATCTGTAAAGCGGTTGCTCTACATTACACACTCCGCTCTGATGATATTCACCTTATCTTGACTTATAGGTAGCCAAGTTTACATTCTGGGGACTGATTTCTAACGTCATGGCAAACCCTGAGTTGACTGCCGCAGGGGGTCTAATTAACAGCTATAAGGTTCTGCCAATCAGTGCACCGTCGTTCATAATTATTTAAACCTAAGACGGGACTGGCGCGTAGCCAGAAAGGTAAGTTCGCAGCCGCAATCAGCACAGCTAGACGACGGTTATTATATACGTTTACTATCCAAGTGGATCGTCCCTCCTCGTCTCGTCGGCTCGGGGTACAGGATGTACCTGGTAACCTAGCGATTCATAACCACATGCGGGGTTACACCGTGGAAGCGGCAGG",15,profileMatrix))

    profMatrix = profileMotifsNoSucc(matrix2)
    #print(profileProbability(kmer, profMatrix))
    print(profileMostProbableKmer("TAGACGGC",4,profMatrix))
