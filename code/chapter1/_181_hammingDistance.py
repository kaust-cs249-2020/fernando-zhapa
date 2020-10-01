##########################################
########## HAMMING DISTANCE ###########

#computes Hamming distance of two strings. String must have the same length
def hammingDistance(string1, string2):
    if (len(string1) != len(string2)):
        return -1
    hamm = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hamm += 1
    return hamm

if __name__ == "__main__": 
    print(hammingDistance("AACCCTTTCCATCTAGACTGGTCACTTGATACCAACGGCCCTCGTCTACGTTCCAGGCAGTACGCCTGTACGGGCCACCTAGACTTTGAGCTAAAGGCCGAATGCAGCCGCGTACATGTTAAGAAGTCTGATCTCGTCGGAAACCTTAACGGGATTTGTCAGCATGCCGTGCGTAGTGGAGACTCGACAAAGTGCCCATTTTGTTCCTGTCACCCCAGGTGTGTGGGTCCGGCGAGTAGTGGTATTCTGACTACGAAAATCGATGCACCGATCCGCTGAGGTTGAGGGAGACAGTTCGATTTGGCTCTGTAGGCTTGGGACTGATTGGGGCGACGAGCACTGTGAACTTCTGGAGGGGGTGAAAGAGGAGGACCTGAACGGTGAAATGCGTGGAGGGCAAATTGATAGGACCGTGATTTCCGCACGGGTAAAACTATTGGTGTGAACCGAGCAAAATGATCCCCGATCTCCTGGCGTATTGAAGCCTGAAAACATAGGGTCAGTTCCAACGAAGAAGGCGACAACGTGCAATTAAACACGTGTAAGTTTTAGGGACTGGTTACCCGGTAATCTTCTCAACGTCACACGACAGGTCGCGCGTAGAAGAGGCTCGCTTGTTCATTCGATAACTTGTCCTACAAAGTCAGACGTGGTGAGGTCCGGGATTGAACCACGAAGTGAGGGTGAGGTTGATAACTAGCTCCATTGGCTCGGTCGGCTACGTTCGTGTTTACTCTCGTGCCAAAATGAATCTTAGACATCCCGCCTCTGGAAGCGTGGCGATAGTAAGTGAAGATCCGTAGAGGTATAGCCCCACGGGTCTCCTCCCAGTTGTTATCGGGGGACAAAGCATTTAAATACCCTGGGGAAATCGGGGAAGTGACGGCCATTTGCTTATGGCGACCCAACCTCCCCTAACCGCGCTCTCAGACACGTAGGACCTGCCAGCTGATGCTCGGTCGCACTTGACCGACCATATAACGACTATTTTTTTACTTATACATAAGTTTACGGTCTAGCATAGGTCCAACAACGTGAAAGACATTTAGATTCCACCAAAAGGGACCG", "GTACAGCTGAACCTGTCTCCTAAATCCCGTCAGGAATCGGTTACCTCTTCTCATCCCTTATCAATGTTCATCTTTCACACTTTCGATCAGGCAGCGATACGTAAGACACACGACTACTTAATCTCCGGACAGCAACCCCTCGCAGGGTTCCACGGGGGGGGGGTCGTCCTGATGACTTCCCTGCGGCCACGAGCGTCCGTTGTGGCAAGAGCCTATGCAATCTCGCATGCAAAATCACACATCCTGGGGGGGCCGGGAAAGTAAAACCCTACTCTTACCGTCCCAAGGCGGGATCTTTGCCTCTGCCTGGCGGAGCGGGCGGCACTCGACCGGACCGGCCTGATCTGCCTATGAAGTGCACCACGAAGGAAGAATAGCAAAGAGAAATGGCGTTGGATTGGTTGATGTGGATTAACTTTTCATGATCTGCACCACCGTGGGTGCGCCTAGCGCCATAAGCCGTTAGTAAGTCCGTGAAAGAATCACCCATTGTCTAAGTGCTGCCCCGCGGGGTCGCGTGCATGCGTATTGATACCAGGTTCAGTAACCCCTGACAGTGACGTAGAATAACGTAAGTCTTACGCGGCCAGAGGTTGTGGGCATGCATAGCGACCTCCCCTTCACCGGGGCACAGTTGTAATTAGCATCGCCCAAGACCCCAGGAGGACCTACAGAGAGGTCGCACGTCGTACGAAAGCTTTGCTTGCGCTGGTTCGCGAAACGTGTCATGACATCGTGCCTTCTGTCAGGCCTCGTTGTCGCTTATTACCTCTATCGTTAAATCATTCCAGGGCAGAAGACCCAGTAGCCCAGCCCCTACAACCTCTAAGGCCCCATGATTTGAAGCGTCGTGTTTTATCCCGATCAAATAGAGTTGTAGTTTTGCGAATATACGAGTCCTTATCTCGGGTCTAAGTATTCAAGACTAAGCACGACTCGAGAAGCCTAAGTCAATGCGTCCGACCTTAGGGAACGTCGTGAAATACGGGTCGTCGTTCTCTTTCTCACCTGTATAATCCGAATTTACGGGGCCTCGCCTGAGGAAACTGTTGTGTAATGACGTAACAA"))