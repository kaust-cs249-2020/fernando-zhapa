import sys
sys.path.append("..")


from random import random, randint
from _231_motifMatrix import score
from _251_profileMostProbableKmer import profileProbability
from _271_randomizedMotifSearch import randomMotifs
from lib import verticalPrint


def profileMotifs(motifs):
    #differs from the profile funtion of _231_motifMatrix because it do not divide by the total sum in each column
    k = len(motifs[0])
    count = {'A': [1]*k, 'C': [1]*k, 'G': [1]*k, 'T': [1]*k}

    for j in range(k):
        for i in range(len(motifs)):
            nucleotide = motifs[i][j]
            count[nucleotide][j] += 1
    return [*count.values()]

def probDistribution(text,profile, k):
    #computes a probability for each k-mer in a string and returns the normalized probability distribution associated with the set of k-mers
    distribution = []
    for i in range(len(text) - k +1):
        kmer = text[i:i+k]
        distribution.append(profileProbability(kmer,profile))
    n = sum(distribution)
    normalizedDistr = [x/n for x in distribution]
    return normalizedDistr


def randomWithBias(probDistribution):
    #computes random numbers based on a probability distribution
    accumProb = [probDistribution[0]]
    for i in range(1,len(probDistribution)-1):
        accumProb.append(accumProb[i-1]+probDistribution[i])
    accumProb.append(1) #to avoid rounding problems
    randNum = random()
    for i in range(len(accumProb)):
        if randNum <= accumProb[i]:
            return i


def gibbsSampler(dna, k, t, n):
    # applys Gibss sampling 
    bestMotifs = randomMotifs(dna, k, t)
    
    for i in range(n):
        index = randint(0,len(dna)-1)
        newMotifs = bestMotifs
        newMotifs.pop(index)
        profile = profileMotifs(newMotifs)
        probDistr = probDistribution(dna[index],profile,k)
        indexBiased = randomWithBias(probDistr)
        newMotifs.insert(index, dna[index][indexBiased:indexBiased+k])
        if score(newMotifs) < score(bestMotifs):
            bestMotifs = newMotifs
    return bestMotifs


def wrapperGS(dna,k, t, n, iter):
    motifs = gibbsSampler(dna,k,t,n)
    for i in range(iter-1):
        newMotifs = gibbsSampler(dna,k,t,n)
        if score(newMotifs) < score(motifs):
            motifs = newMotifs
    return motifs

if __name__ == "__main__": 

    dna = [
        "AGACGCCCTGGTCAGGGGTGAACACCGATACGCTCGGTAAGTGTCTAATAACCGCCGGGCAACTCTCACAGCCTGCTCATACACAGCAGACGAGATCTCAGTTGGGGACGCGGCATCAGGTAATAAATCGAATTTATCTATGATCATAATCCACGATCCTTTAACAAACTAGTTAACGCTATGTTTGGGAGAACCAGCTATGCAACATTTGCGGTGCACCGATAGTTTCTCGGTACGAGTCCGACGATGGTCCATATTTTGGGGCAGCAGATTAACTCGCCGTGCTTAAACGGCCGATAGTAGGCCATGTCCCATTAGACGCCCTGGTCAG",
        "GGGTGAACACCGATACGCTCGGTAAGTGTCTAATAACCGCCGGGCAGGACTTCATAATCAGACTCTCACAGCCTGCTCATACACAGCAGACGAGATCTCAGTTGGGGACGCGGCATCAGGTAATAAATCGAATTTATCTATGATCATAATCCACGATCCTTTAACAAACTAGTTAACGCTATGTTTGGGAGAACCAGCTATGCAACATTTGCGGTGCACCGATAGTTTCTCGGTACGAGTCCGACGATGGTCCATATTTTGGGGCAGCAGATTAACTCGCCGTGCTTAAACGGCCGATAGTAGGCCATGTCCCATTAGACGCCCTGGTCAG",
        "GACGGAGTGATGGCAATAACAACTCACATGTCGCCTCGTTACGAATCCTTCAGATGAGATCATTGTGTCGTCCCTAGCCAGAGTACTCTTAAGACCGCTTAGCCAGTAGCCCCATGGTCGATTATCAGTCATCATCTTCTAGTAGACCGGGGCCCATGGGGGCATTGCCCGACTTCTACGTGGTACAGGTGCACTAGAAGTACCGTAACAGCTGGCGGGGGTACTGACGTCCTTCCTGAAGCCATAATCGCCGGTGATAGGCCACGTCTACCCCCGCGTATTAGCATTTGTTCCATAGGCTAGTGCTTAGACAGCTTGATTTGGGATCTAA",
        "CGGGAAGTACTTAAACTGCAATTGTCCAAAGCGTTGCCCCCGTTGCCCGGTCCTGAGTCGAATACAGTAAGGGAATGTCGGGACCTACTCTATTCAACAGTGTTTAGGCCTGCAAATTGACCCGCTCATTATAATCTGTGCAGCTTGTGCCTCGGAACTCTCGATGTTCGCGAGCTGAACCCGATTTGATTCCCGAAAAAAATGGACAGTACTTTGTCCTGTAAAGCAACGCAGTCGACCACGCGCCGGCTATTGCTGAATACTATACGTCACGTGAGTTGCTCCTCTCTATCCGGCAGTTCGTTATTATAGTAAAAGCCATAATCAATTG",
        "ATAACGCGGAAAACGGGCGCTCGTGCTCGGTTCTCCAAAACTCCCAGCGTGCCATAATCAGGGGGGAGGTTGCACTGTTAGTGATAGAGAGTCGCAGCCTCAGGCTACAGATCTAGGCTCATGAGAACGTGCAGACGATGATCAGCTGCGATTGGTGGGTTCTTGGGGGTTTCTTCCCTCCCCAAAACTTCATGTGTTACAATATCCTAGAGGCGACACAGTAGCTCGAAATTAAGTGCCCTCGGAGAGTCTATCAAACGAGCGTGCTAGGAGCAGGCAAACTGTGATATTCCCCGCGTAAGGGGGTATCGGGAGTCGGGAATTGATAGAT",
        "GCGTGTCCCAGAACCCCGTACAAAAGAGAATTTCGTGTAACACAACGTACCAGTGCTCCCACTCTGGTGATCGCCAGTTGGTCGGTAATTAAGATTCAATACCCTGAGGGTAAAGGCGCGTAGATCACGAATCTTGTGCCTTACTCAGTAAGGAATAAATAATCAGAGGCATCCAAACGTCTATTGGTACACAGTTTCGTTAGACCCTTGCGCCTGCATCTGTTCCCGGCCTTACTGACAGACCGGAACACATCAGCTTCTGACTAAACCCAGAACTGCGTAATCAACACTGATCCGAAAGGGTCTACATCTCATCAGTAAGGTGGGCTGG",
        "GGCACTGTGTTCCGCTTACGCCTGGGAAAGCGTACCGCTTGATAGGAGAGAGGTTCGGAGCGTGAACAAGGCATGGTCCCGACAGAGTTCGTATAATGCTTTGAGTCGAGGAGGCCAAGCACCACCGAACAGGTTTTACACGATCCCGCCAAACGGCTACAGGGAATATGCCGTCACCCTCCCCGTTCGGTTAATATCGAGTGATCACAGTAGCACTTGTGATCAAGTGTGCGTGAGCACCACTGCTGGAAGGAGTAATCAGATCTATCGAGAACAAGCCCTGGCGCTAGGATGATTCGACCTGCATCGGGAAAATACTATATCTACGCTC",
        "TCCCTGTACGCCCGGTGGAGCCTTAGGTCGACTCACAACAGGTTCACTTGCTAACTCAGTCTCGTGCTAAGTATGTACGTTACCGGGTGCTCGGAAGGTGATCATTACGTGGGCATTTTAATTCCAGGCCAGTTGTGAGTGGCAGTCGAAGTAACTACTAGACGGTAGAGACACCGAAGATAGCCCGGTCTTCTAGGTGTTGCAACGCTCCAAGGACCATGACAGGAAGCCATGGGCAGTATGAACGTGAAATTGATCACACCACATAGGTTGTTAAATGCCGGGGCTGGCTATCTCTCTTCAGGCTGATTCGCAAAAGACTTTGCCATGT",
        "AGCCATCGAGTCTATTGCACCCAAAACAGTATAGACAGGGATCCCGACGCAGAGTTTCGATGACTATGGTCTCGACAGTGCCGCTCAAAATGATACGTAGCAGTCCCACTGTCACTAGGAAAGGAGCAAGTCTGAGATAAGGAACGTTGGTATCGTTATACACCGTTTTCCAGTGGTTAGCCCGGACCGTCGGGGAAGTGCTAATCAGACGGCGCGCTGTATATTGTGTTCGCTCTTTCCTCTCTTGCTCCATAGAGATCGTTAATGAGGCGGCAACTGCTACCTGGCGGTCAGGAGCAGGTATTCTTCCACATGCATTATTCGATCACAT",
        "GGGCTCCTAGATCCCGATAGAATGTGGTCCGACGAGCGCCCAGTACACCCTTCGAAGATGTTAGTCTCTTGGAAATTATAATCAGGACCCACCCGGACTGTTTCACTGTCGAATTATCCCTATAAGTCAGCGGTGGGATCGCTTTTCTTGGACGCTCCCGACTGTGTTAGGAGCTGGGCATACGTCGAAAGTAATGCTGTGGTACCGCCGGGGTACACTATCAGGCGGCTGGCACCGCGGATTTACTCCATAGACCCTCCTTTGTAGGGCCGGTGGGACCTACACGTCCACTATCGCGACCCAGTCCAATGCACACCATCTGGTTAAAGTG",
        "CCGCGCAAGACAGAGACGTTGCTGCAAACGCGTCGATAGAGTATCCGAGATGTATGTAAAGCAGGTCCCGCATAAAGCTACAGGAGGCCGAAAGGATGGGATTGCGGATCCTATTTAATTAATTATCCGGGTTTAAATGGTCAATCAAAGGCGGCTTCGATTTCGTATGTTCCACGGTTGGCGCTGCGCGCTGGTCTACGTTATCAGATAGGATCGCATAATCAGGAGCATGTGGGTTTTCTGTAGGGTTCCTGCCTGCCCCATACGGTACTTAGGACTCCGTACCGACCGCCCGTCTCGATGTGTGTGGCGTTCGCAGAAACCGCATTGT",
        "TCCACGGTTGGAAGCCTCGATCAGCCTTCTGTAAAGCCTCCTCACCAGGGCGCTCCCGTAGCGTATGCTATTCTCAGGGAGCCTGCACTAAAATCCAAAACTCCTCTGAACTGCACTGATCTTGTTACCTATCAGAGATCGCAAAGTAATGTGATTGCATAATAAATATCAGGTTAGTCGTGGGTGAACCTGGTTTTAGGTAAGCGGTAACGTTTGACCTTGGGCAAGGATCCCGGGATGAACCTAAGTGTGAAACTATGTTAAGGGAGTAGGTATCACCCAAGGATGAGATATGCATAATCGTATTCCTAAGCGAGGCGATTTTCACCGC",
        "ACTTTACCGAGTAACGACTATTCACGGCCGGTCGTGCAACGAAATCCCTGCTGAATTGGACCCTGCAGAAGTGAAGCATAGTTGCCCTTCTTCTTAATAGCGCGGTAGATACGTCGGACCAGTTGCTCTCTCAATTGTTGTTTGAGGAAGCGATAGTCCGTACGGTAATTCGATCATGAGGTACCAATCAGGTTGAAACCGAGATTATACACCTCTAATATCTGGAATCCTAGATGGAAGCCATAATACAACCGGCTACTTGCGTATTATCTGCAAGTCCTTCGATGCTTGACGGTGATTGGTACAGGACCCCGAAGACGGTTTTCGGCCG",
        "TTGCCTCCTGTAAGCCCGGGATGGTTGAATGTCAGACACGTGGGCACAGACTTATCGATGGGAAAGGTAGAGTCGAAAACTCTCCTCGTTTCTTCAACTATATGTTTGCTGCTCTAGTGTAGAGCGCGACAGTCTCAGGTTAGAAGTTACGCGCTAACGAGTTTATACATCTAAGAAGCGGGGGGTGGATTACATAACGGTAACAGACCAGACTAGACGGTAAAACTTGTGGTTAGGATTTGACTTAGGTTCGGGGAAGCCAATGTCAGCGACAGGGTCACTCGAAGCCTCGCATTCTTCGTCCAACGGTCATTAGACTACGGACCATAAC",
        "TTTTACCCATATAGGTACCTTCGGCGCAAGTCAGGCTTTCTCCTTAGCACGCTGACTCTGCTTATAACATCGAGGCAAAATGGACCCAGCTTTGCTCGACGCCTACCCTGACCGTGTTGGCGCGTCTCTTAGGATATGACTCTATCGAATCTAAGTCGCGCCGTAAGTAATAGGTCTACCGGAATAATCCGGTAGCTTCTCGCTGTACGAGTAGCGGACTCAGTGGCAACAAAACAGGATGCACCGGCCGTTGGGTTTTTCCACTAACGGAGGATGAAATATTGGCACATAAACTCTAGCGAACCGAACAGTAACTAGCCATAATCAGCTT",
        "AAGCTGGAAGCCATAAGTGGACAAGCTGAGACCAGGAGTAGGTTCCTGACCTTCATATTGTAAAAAGAGTCACAATGAAGTCGGGCGCTGATCGGCTGACAATTTCAGTAGCGTAATCGAAAATACAAATGAGGTACTCCCGATGCGTGAGGGGTCTTGCTACCGGCGCAGCCCCTGTGTTAATCTGAATCAACTTGTGGGGCAAGCGTGCTATAGGTGATAATGCGGTTGCTACAGACAAGGGAAATGGGTTGTGGCCACAGCTCGTCTGGGTGCTAGTCGTTAATCAGCTAGACGATCTTCAATAGTTATTGGTCGGGATAGATGGCAC",
        "GTTCACAGTATGAGCGAGTGATGTGGAAGTGGGCGTGAGAGTCTAACCCCGAATGCTCGGCGCTTTTCTAACGGTGGTCCTAGAAATGTTGAGGGTCAATAGAAATTTCCGGGCCTATGCCGTAAATTCCGACAAATTCCTCAACTGCCCGATTACAGGGTCTCCATAATCAGCGTAAGTTATGAGACCTCGCATTATGCACCTACATGAGTGGTCCTAGACAGCCACTAGTGTTGATACATGCCATGGTTATACAACTCACGAGGACCCAAGAACACACAGGCCTACTTTCAGCAAGCAATCTCGTCATTCTTCTATACTTTACGTCGGC",
        "ACTATATCTCCTCATTGTCCACGTTCTCGCCCCTCGTGAGTCAGGTGGCGGGAACTTTGGCCCAGCCAGTTTTCTTCAAAGGCTTGGGTATGTAATTCGGTACGACGTTCGGCTAGTAGTCCTCCGCCTTCGACCCGTTAGCGAGATAGGAATAACCACGAACTAGAACAGTCTATCGACACCAGAGACGCGTGCGCCTCGTTTCACAACTCTGTAAACGTGCTACGATCGGAAGCGGCAATCAGAGGTTGCATGCGAACTCACCGTTGAGTCCGCGCACACCCGCCTGTATATTAAGCTTCGATCGCGCAGCACCGTCACCAGCGGTGAT",
        "CCCATCGTGAAATTCCGTTGGAAGCATAAATCAGCATCCGTTGACGCTGTATAAAGGCAGTGAGTCGAAGAAGCAAAAATCTAAAATTTTCCACGCGTGCAAGTTATCGGCCGGAGCAACTGTGAGCAGGTGCATGACAAGGTACTCGTAGTGGCTGCATCTTACTTGACGGCCACCTGATCTGACGACCCCCAAACTTCGCGTTCAACTTCCTTGGGCTCAGTGGATACGCCCATTCGCACGCACACCTAGTATAAATCAAGTAACTGTGTGTTCCCCAAGCTGTTATGGGCATGCTGGGGCGATGTACCAAGCCGCCAATGCATATTCG",
        "TAGCTGGGAGGCTGTGAGTTGGGAAGCCATAGAAAGTTTCCTGGGTATCCGTGGGGGAGTATCGGCCTACCGCGTTTGGTATGGTACGGGAATAGGTCCACATGCGTGGCGTCAGGCAACTACACTGTGACGTGAGTACATTTTACACAGGCTCAATTTGTGAATTCCGTTCTCATTACGGATCGTTGGATCCGTTCCACACGGTGTGTAGATGGGAAATGGGGCGAAGGCGCTGGGTTAAACGTGGGAGGCTTTATGAACGTCCTGGGTAATAAAGGAGAGGCAAACAAAACTATGCCTTTGACTTGTTTGAATGGCGCCTCGGCCCTAC",

    ]

    verticalPrint(wrapperGS(dna,15,20,2000,20))