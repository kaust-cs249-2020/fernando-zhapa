import sys
sys.path.append("..")
from lib import spacedPrint

from _181_hammingDistance import hammingDistance

#finds the approximate occurences of a pattern in a text with hamming distance less or equal than an integer d
def approxPatternOccurrences(d,pattern, text):
    patternLength = len(pattern)
    positions = []
    for i in range(len(text) - patternLength +1):
        if hammingDistance(pattern, text[i:i+patternLength]) <= d:
            positions.append(i)
    return positions
    
if __name__ == "__main__": 
    spacedPrint(approxPatternOccurrences(6, "TAGACACTT", "CAGCATACGTTACAGATCCCCGACACAGAGACCCAAACTCTTTTAGCCAGGTGCGCTAGTCCCTAAAGCCCGTTGAATCCGAGTTTGTTAAACATGTCTCACTCGCTGATATAGTACGAACACTCTCTCGCGATAAACCTTTGAATTTATCCTGTCATTCCAACGGGAGGGCTATATTGCCTCTCAAACCATCTCTAGATTATCCCTTCTCGGCGACACAATGGCTCTGGAGCTGGAGTCGAATTAAGCGCCTACAAGTATTGCGAACATAGACGCATTGCGCCAAATCGGATCTTCCCCTTCAGAATCGCGGTACTACCCTCCAGCAATCACACCCGATAGACATGGGCTGGCTAGCCACGTTTCTCCTAAAGACTAGTGTATAGAACGCTCTTCATTTTCCTTCGTAAAGAAATTGCTGATGTCTTAAAAGACCTTACCGACACGGGGGTGGTGCGGTGCCCACAGTAGGTACGGCAGTGACCTCTCCAGGAGTGAGCTGCGGCATTTGACTCATCCTATCGTATGTCATAAGACCTGCTAATAACGGGGATGGAAATCCACCTCCCGGCACCCAAGTTGCAGGTCAGGTATCGACAAACTACGGCGATGAGTCAGAAGACTGACTTAATAACCTCCGGATCAATAACTTGTGCTCCTGCGCATGGTGGGCACTTTTCAACAAAGTCTCATAGGCTAAGGGGCACGTAGGACCGGACCTGTATAGCATGGGGTTAACACTGACAAGAGGGACAAGCGGTGCCTGGACATTAGGATAGCTCTAGCTCCCGACAGAACACATATGATTAGCCGAACCGCGGTTTAATGTCATGAACTATCATTACTCAGGGATACATGGCCGTCCTCCACGTTGCGAGCCGCTCCTTAAGTTACGGCAATGCCCATAGCTAGTTTAGTAGTCTGGACATTACTGCTACCCCTGGAATCAATGGGAGGCATGAGGTATCGGTTTGGTTCCCCGTTTAGTCTTACGGCACGGCTCTTGCCTACGCATGGCTATGAACAAGCATGCACTCACAGAGTATCTCAGGGATGTTATTCGACCTTCATGGGGCACAGCAACCTGGCATAACATGCGCTCACCGGTAGCAGTTACCCTACGCATTAACCCACCAATACGTGGCATGTAAATTTGTTAGCGACGTGATACCAACCGATTTGATGGTCTCTGTTGTGGGTATGAACTGGTAGTGCCCCTTATACCGGCACAGACGCTCTCATAGGAACCTACCGTACTTAGACTTTCCACGGAGACGACGCATCCATGCATGTGGGGTTCCTAGCAATGCGTAATTCCGGGCCGGACGCGGATGCGCTGTGCCACCCCAGAGATTGCGTTGGCATTGATTTGCCTTCGAATGGCCTATTCGACAATTGGGTACAAGTGTCACAGTGAACCCCGCAGTGAGGAAAGTGCTGGGATCGTGCTGAAGTATAGGGTGGGATTAATGCAACGAGTCCTGGAGTCCGAAGTCGCATCGTGTAATGATTGCCTCCGGTTGCAGCTGCGAGTCATCCCCGGTTCTCCCGCGGTCAGACGTTTTCGGAGCTCCTCGGGGGGTATTGCAAGACGGTAGGGTTACGAGTAAAATGACTATCATAGACTGACGTGAGAGGGAGCGGAGGTGTCTGTGTCCAGGCGGACCCAATTACACCAGAATGCTAATTTGATGTGGACAGATACTGGCACGCAACAGTCCTCCACATGTATGGAGATGCCAAACCAATACCCTCACTAGGGGTTTCACATCACTCAGGCTTCCTCGTTTGTACCGCGCATACTCACTCGCGCTCTCTACCGTCAATCTCCAGCCGTAGCCGGCTGTGGACCTCAGTAGGCCGGTTAACGCAGTTAGACTAAACCGCCATGCAGCTACGGCTCCTAAGCCTGAAGTGTGTTGCTCTCTTCATATCTGCGGATCGCTTCCGTTCGGAAGCACACCAGGGCTGATGTCTCCTCTACGAAGAAACCATTCGCATACGCGGATTTTCTCGGGAGCTGGTCAGTGTGTTGCAACCAATTTACATCAGAAGGGACCGGACCTTTAAGGAGTATATCGAGGTATGTTCATCGGCACTCAACAACATAGCTGGTATCGGTGTGACACTGTTGGCTTTGCCCAACCCTTAAGCCGAAACGAGCTCCGTGCCGTAAAGCTAAAAAGTGTAAGGGAACCGGAGTTCCCGTTAAGGGCGTGCGGTCGCGATCCAATTCTCTCAATGGGGACGACCAGCATGCGGATTCTGGTTTTGCGGAGCGAAGCGAACCATAGCGAAGGATGTTGCACTTACCACACAGCGCTCACGAGGCCTGAACATAAGCCTTTGCCTGGGTATCCACTGCTACAGATGACAGACTTTAATGCTCTAAGTCGCTCTGGGCGCATGCGCAAAATTCTGGACTCGCCCTCGACGCATGTGAGTGCCTAGTTCACACGTTTGCTTTTCACAGTATTTTCTCTCATACGTAGATTTGGGATACTTCCAGAGCACCGGCGAATGCAAGACAGCGCCCGACACGTGACGAGTTGTCCGATTTCCACGACACACAAAGTTGAAGCAGCAGAGCCCACAACCCGGCTCAGTATACGGATCTAGCGGCCCGAACGAGCCTTGACAGCAAATAAACGATAGCTCTCTATTAGGAACTAAATTTGATGTTGTGGACAAGAATCAATCTACTTCACTTTGCCACCTCTTCCGCAGGCCATTGATTGATTGCGCACTATAAAGAGCCGTAGGATCAGAACAGCGCACTACCGTTGGGGATCCGTCCTTTCGGACGTGTGCACAAGCACACCGTTAGTCCGGAGAGTTATCTCCTCAGGAGTTGGTAGTACGCGCCGCATGTGAACGGCGCCTCCTCACTCTGGAGCTATCTAAGCCGGTCCGGTTCGCGGGGATGCCGTATATTCAGAAGTTGGGGCCCCGGATGCATGTGCTCGGCGCCACTCGGGAATCTGCGAACCAGGGAGCATGTAATCCATGAAAATGCAAAAAGTATGGCATGACCATTACACTCCTTAGCTTACGCTTTCGCTCTTAATAAAGAGCGCCCTCTGGTCTTACCTAATTATGGCTTTACCATAAGCCAGAGTAAAGCTTGTATTGCGCTCGACGCGAATTGAAGTCGTATCCCGCCGTAAGGAAGATGCTGAGGTTATACCGAAGCTGATTCGGGTCACACCTCCAGCGTTGATGAGTTTTAGGGTGGAGTCCAACAACAGCGAACGAAGCGTTGCGCGCCCTATCCGCGCCTATATGGGTTGCCTTCAATACCTGGAAAACGTGGCGTGAGTATCATTCGCGAAGCACTATTATTTACATAGTTGTCTCTAATAGTGGATCATGCATCAATGTCTCACACACAGCGCACACGGATACGTATACGCGGGGACTACTCCTCAAGGATCATGCACGGATTATAATGTAGGCATCAACGTTTCGCGACTGGCCACACGCACTTCCGACCTGTGGACCCTGCTCCTAAGATACCAGGTTACTCGCAATCCCACACGCATTTAGTTAATAGCAGCACCTATATGAGAAGCCCGCCTCGGGTCTCTGTACACATTAGTCCAGCGGAAGAGCCGATGATCCAGCCGGACATCTATACTCGGTGCGAACTACCAAGCGAGTTCCTTGACAGCTCATGCCTCTCGCATACCATAAATGCGAGCCATGACCCGCAGAGGAATGTCAACCAGGATTGCCGTGTTCGCGTTACTGATCCACTTACTGTCAGAATGAAGCACTCAAATAAGCGTGGCATAGAACAAGCGTGCGCCGAGTAGGGCTGGTTGTCAGAACACACACTGCCTATAGGAGGCAAACTTCTGGGGGAATGCGCCCCTAATAGGTGGGCTTATTTCCTACGCATGTCATAAGCCGGTTCAGGTCGGCCGAACGTGCTTATATATTCCTTTCGCGCCGACCGTACTAGCTTTGTGAAATGCCAGTGCACGCCCCACTAAGATTGGATCCTTGAAACGATGCCTGTAGGTTCGCTTAGTGTCGACCCACGAAGCGGTTCCACTGAACGGGCAAGGTTTCTGCTCAGGGCGGGGGGCCTATGAAGACCCGGAACTAAAAATTACTTGATACCACTAGAGCTAGTGTTGTCCCCTGGATTTCGCTCATCCGGGGCCCCGATAAGTAGTAGCACACTCTACTATCGAGTCACCATAAGGTAGGCGCGGGACGTGCAACACCTGCCCCACAACATTTCTTTTGCCAAGCATCATATTTATATTCCGGGAGAAACTCTGTTGAGCCAGCGAAAATTAGTTTGATGTGGCCCAGCTTTACCTTTGTAACCCCGAATGTAGCCCGTATTAGCGGTGGCACAGTTCTATGTACCATAAGTTAACTCTGTAATCCTATCTAGTTAATCATGCGAGTAGTAGGACAACTAAGATCGGACGTTGTGCAACAGATTACATTGGTCGTGCGAGTTAGCACGTCAGGGACGCGTTTCAGGGTGTTCCGGAACCCGGCTTCGGCTGAAAGGAGTAGGGTTCTTGCCAACATCCCAAAAGCGGGGGATGCTTAGTAGCTCATTGCCACTAAGACACCAAACGTGCTACCATCGAACCACAGACTCTCTGGTACATACGTTACCCCCAATCCCGGCGGGTAGTTCTCACTGGTGCGTTGCATAAAGACTACGGCCACAGATCGATCTTGGCTTTTGTGTTGTAAGCTAGTGGAGGACACATAATTGCGACGCAACACAGCCACACGCACCCTGTGCAGTGAGTGCTCGCCCACACGTAGATCCGTGGCTAACGAGGTACCGTTCTGGGCAGCATTATCACTATGACAATTCAAAAGAGAATAGTACGCGGGGGCCCGGTAACGTCATTACGATACGATTCCCTAAATGTCCGAAGATTGACAAAGTATAAAAGCATAGGCTGAACAAGGGGGTGCTATCTGATAGGTGTGTAGATGTGTTTTCGACGGTCGAGGCCGAACGGTGCAGATCCTTTGGGGTGACTTGTTCTCCTTGAGTCGCTTGCTATAGACTTGTTTAGTGCGTTACCTTGGAGCCCGGGGTCTCCCACGATTCTACAACTCTCCTGCCTTGTGGCTTATCAAGTTCCTAGATGAAAATTTTGACGCCGCAGAAACTTCTCGCATTTTGTTGAGTCCGTCAACCACCGGTTTATTTTATACCGGTAGGGTATAACTCTGAGTACCAAATACGGCGGACCGTCTCAGATCTACCGGGACACGGCAGCCAGCCCTGGCATCGTTGAGCTTCAAGCGAAATTAGAAGTCTTCTGCCGTGAGGTGACCATCGATGAACTGAATAAGGAGCATGAGGGCTTTCTGACAGGCGTATACTCGAGTATAAAGTAAGCATAATCCCGCCATAATCGAGCGTGATTTCTGATACCACGGTTAAGCATTAAGAGACAGCGGGTGGATACACCCGCACAATGGTGGCAGACTGATCAGGCATTGCACGAGTAATATTGCTAAAGATCGTTGTTTGTAGTCTGGCTCAATGTGTCGGCTGCCTCTTATGGGTTAGGGTATGTCTATAGCCGTGTCTCCAACAGACTGATCGCCGTCTACTCGAAGTTCACCTGAATAAGTATGCAGATTGGTACCCATTAAAAAGCGCTACCGAATCTTTCTGTTCAGACGGGCTTCTACGTCTGCTGTTGTAAATCTACGATCCTCTAATGGATCGGGGCCGAAGCCAGTTGTGGGTGACATAATACTGCTTACTCTAATCGCTCCCACCTACCGAATGCACAGAATACACTGACTAATTCCGGCCTACAAGAAAGCTGTTACCCTGCCCCCTTCGCAACATCTGAAACCGAGACCTTACCCCGCGGATTCCATCCAGCACCTTCGAACGAGCTACTATCCATCCAGAGATACGTGTGACTGCGAGTTGCAGACCTGATGCTTGCACGCCGAGTGCCTCCTGACTCGGTAACAGTTGCGGTTTATTGCATGAACTACCGCGCCCCTAATTAGAGCCTTCGGACTTGTGATATTGTAACGTATGATCCTCAAAACCCAAAACGCGTGGACTTTTGGGTCACATCCTTCTAACATAATCTTGCCCTTGCAGCTTACACACCCGGAAGTATATGATAATTCTTTTATAAAGGAACGTTCATGGGGAGGAGGTTCGTTCATGTGTAGACAACCGTTATCACATCCTGGCCACCACTGACTGGGTCTCGCCCTATGCTAACTGGGGTTATTCGTTTCGAGTAGTATCTTGGATCTACGTGCTTCCTAAGACTCATAAGCGGTCGGTTGTGCCGTAATCGCTGCCGGAAAGTTGAAATGAGACCTACAAACTCGTCGATGGATCTTTAAGAACGTTAGAAGACCAAGAGGTCGCTAGAGAGCGTATCTTAAGGGATTCATGGGCTTGCGATAGGCCCTTTGGGCGAAGGAGAAGGGTAATGACCATTAACATTCTATATGTTATTGTTCATATTCGATCAACATCCAATTTACCGAAGACTTGATCCGAACGCAATCCCCTAATAAAGGTTGGAAACTCTGGGACGACCAGCGACTAGTTATCCGGAGGCGGGGGAGTTAGGGGGACATCTGGATCATCACTCCTTCACTGGACCTAGACTATAAGGATGTGTTGACCCCGAGTGACCTTTAACCAAGAAAGCACAAGATACATAGGCCCTTAACTTCTACGCTCAAAGGCAACCGCCTGGGTCTCCTATCGCGGCAGTATGGACAGTTACGCTACTGTCAACTCGAGGGTTCCCCTGACACGGCTTTGGTTATTGAATACCCACTTTAAGAAATGCCGTAGAAACGCTAGAATGGCGCGAAACTCACAAGAGCTTGAGTTCCCTTTCGTGAGCAACTACCCGGGTCGGCAGCAGATTTTTATCTCTGTCCCCCCATTCGCCCCGCGTCTTTTTGGTATAATCCAGGGTAGAGTTAACTTGCCATTTCATAGAAGTTGTCAGCGCTGCGCCAGATCCTAGTTGCTGCGTGCAGTTAAACATTGTTTTCCCCATGCCGAGATACCTATTACAATACGCTCCTGACAGCTATACTCCTGGCGGCGGTCCCACTCCTCAGCACAGGTTAGAGCGCTCCACAGGCATAACACACACACCGGCCTGTCTAAATTCTAGCGTGAGGTCACTTAGTTACGCTGTCTAATCTCACTGCGCATACATACTGCATTTTGAACTCGTATAAGGACGCGAAATTGGTGTTATACGGCCCGCTATATTTGACCATTGCAGAGCTGTTATCCGCCGAGCTGGCGTATCCCCGACCTGTGATGTAATGCTGCACCATCCTCCAGTCGTCGGCAACTCACGTGCAGCCGTACTAATAGGTGTCGAAACGCTTGCTCGAGCAGGCTACGGTAGGACTCTCGCAGCATGCCGATCCGACCCACCCTTGGCATCGCGTCGATCCAACCGAGAACTAAGCCTATTTATCCCCCATGGGATTGGGTTTCCATAGCCTAACGTAACGATAAAATATGGAGTAGACGCACTGTTTTTATACAGCTCATAAGAGAGTGGGGATCCGGGCTCATGGTGCAGCTAACTGAGGGGCATGATCGCTCAAATACAGGGATATACCGCTTAATGAGTGTGTTTTGGCTTGCTGGGTCACACCTAATCGCCTGCCTAGGTCAATACGAAGCCTCATCGCAAATGAGCTCGGATGGTGTGATAAAGACAGCCTTTACCGCAGGACGTATTAACGCTAATTACCGTAGCACCTGTATGCGGGTACCGCTTTCATCATACTAACTTTGTAAAAGATAACCAGAGAAGCTATAGTAGCTGTGCTCGGCGCTAAGCGTAGACCAACCACTCCAAATACATTTAAGGTACTTTCGCCATGAAAACAGTGATTTGAGCTATCATAGGACGTCGAAATTTACTATTCCCAATATAGCCAAGTTTCACTGGGAGCGGTAGCCAGCCCCCTCAGGGGACTCTGCACCCCATGTCATACCCAAGAAGACAAGAGCAATACATCGGCGTGCTAGTCCAGACCTAATATCAATCTATTGGCGAGTCAGGCTAGAACGACTCAAGAACTCAGCTCAAGAAGCTCCGAGTGACATGACCATCACGGTGTCTTGTTCGATTTGCGTGTTTAAGACCGCGGATCTCCGAATATCTTGGTCATTACCCGCCTCCGTTAATGTCGGTCATCATTCCTGACGACGCTTGCGGCGTATATAACTAAACGAAGGGGGCTATCTACGTCACCCTGCCTTGGAGCACACGTCGTCTCGTAGAGGGGTTGTTTACGTTTATGGCAGTCCCTTGGATGCTACTGGAGTGGCGAGTTGCAGTCTTGATTATGCTACTGTGTAAACTACAGAGCCTAGCGCTATTGGGCTTTAAGTCGTCTCTAGGCTGCGCGATGGCCTGTGGGACCCACAACGACCAACGCCTGCACGTATTTGTATTGGCGGGGACTTGCGGATCGTTTATCTAGTTTGGCGCCGGTTTAAACGCGGTTCGACCTTCCGTAAACTTTCTACCGAGGTCATGTCACTAAGAATGATCCAACGTTTTACACATGTAGGTCGACATATTCTTACTCAGGCATTAGCGCCATCCGTAAGGTCCGGATCCTCGTGACGTCTGATAGACTGTTTCATCCGGGCGAAAAAGCCCGAATGTTCGCTTTAAGCCCTACCCCTCCCTCCGCAATCAAAGAAAGACAACGAAGCGCAGCTATGCGGGAGAAGACTAATCGGGGGCCTTACTTGTGACTTGAGGTGACTGAATGTTTCCATGAACCGTTCACCGGAAGGTGTGTTCAGTTTAGCAAGGTCCGACGAACCTGTATAAAAGTCCATTATCGTTATGAAGGCGGGGCGGACAGTATGAGGAGCGCGTATATTTCAGTCATTTTTCGGTCTTCGGCGCTCGATTCTGTTAGTGTAGTCATGGGTTAACCCAGACAGGTGTGTGCCAGCTGCCACAAGCTGGACCTCATGCTAGTCCACACGCCCAAGACTGACTAGTGTGGTAGCGAGTTTACGGCCCGCTGATTGCATCTTGTTATACGTGAGTGAAGAACGACAAAGCCAGCTTTTTCCACGCTTAGATGGCCAACACTACGGCTGTGAACCGCTTGCGTTCCGGGGCACGTCCTTTGCTCGATCTGGAGCGAACCCGATTAAAGTACGAAACCGTAGCACCAATCCCTAGAGTGAAAGGTATTCGGTCCGGGGGATCACAAGATTCGTGATCACGTCGGGGTAACCGGTTTCATCTTTCCGGCTCGAAAACCAACATTGCTCATACGACCTTCTTTACGCATAAAACTGTCAACCACATGCGCGACGTGGAAAAGTACGCACACAAGGAGGCGCGCTTAAATTTATTACCGCATTTCTCAATTGACGTGGGTGAGGCTGTATGGGCTCGACTACGAAGTAAGCCCTTGCATTTGTGATCCGAGGTGTACGGGTCTTATAGGGGTTTGGGCAGACACGGTAAAACTGCAGCGCCGCAAAACATCTGCGTTCTATGGGATACCCTCTATTTTTCACCCACTTACATTCCCAAAGCGAGAGTAAGTGAAAAAGCGCTGTCGGGGCGCAGACTATTCCTCAGAATCGCTAACCAGTTACGACGACAATTTCTCAGACAATATATGTTCCGACTATAACCATCAATCGGCCGCACCGTGACGCTGACACTACTTTCCTACCGCCTATCACGATTAGTTATAATAGCTTTACTGGATGCACGCCCGACATGCTCATAGTTTGGACTCATGTGGTAGAACTGCACACTCTCCGTTAAGCAAGCAGGGATTGCGCTTCAACGTCGTCAAAACACTCGAACTTAGCGACAGGACTTAGGTAAACGTATGTGTTGTAAAAGACACTTGCAGATTTAGGTGTTAGTGAAGCTCGGACCCATCAACGGCCCATTATCCCTCGACGCGTTAGGTTCTACGCTTTAGGTTCTCGGAAAATAACCCGGTTTCGATCGCCCTGCGCAAAACACCAAAGTCTTGAAAGTCCATAACAGTGGTCTTGGTTTAAGGCTACGTGATCAACGCCGTGGGATCTTTTAGGACGTAGCGGAAGCGCGGTCGTTGACTATTTTCACCTGCCCAGTCACCCCGCCTAATACGCGATTCGGACGTGGCTAGGCACTCAAATTATTAGGAGGTCCACAACATGTGATGTGCTTGTACAGGGCTGATTTTCTTCAGTACTAAAGTCGCGGAGACTAGGGCGAAGGTCAATGTCTTAATCCGTCTACTGTTTCTTCGCACGGGGTGCCTCGAATGACAGATTATCTTGCACCGACAGACACAAGGCCTAGAGCTGAATAGTGAAATTCTTATGGGACCCGTCAAGCTAGGTGTTTACAGAACGGATAGTAGAATATTTTAACGTCTGGCGTGCTCGGGCCATTGCTCAATAGATAGGTCTTGGTTTACCCATATAACACCCCTTGCCCCTGGGTAGAATCCGGACACGTGGTCCCTCGATACACCATCAACGGCGCCGGTCGGAGAGGTTGTCGGTTCATTTATTTTGCGTAATCAAGCGTTGGTTCTCCCGGTCTTGTAGGCAGCATGGCCAGTCTCACATTTCATCCCGTCTCAGTAGGATAACTATACGCAATTAAGGAGTCTCTCCCCACGAGTTAAAATTTGATGAGAAGGGCGCGGATCTTATGGAGTAAGGTATAGGCAACGTTGGACTGTTTTCGCCTAGAACCAACTCTGAGAGAACGATAGGTTGAGATAAGAGTATGTGTTTGCGTGTGCGTTGTAAATTATCCTTGTCATCTACCGGGTGTCAACTACGGCGTGGGTCCATAATCCGTACGATATCGACGTTCCACCCCAAAACTAGTAAACGCGGCTGCGTTTATAGTGGCGGTCTACCCCTTATTTCGTTACGTTGTCATTAGCATCGTTTACACAAGACAAAGGCCCTATCAAGCGGAGGATAAATGGTTTGGCATTCCACGCTAAGGCGTTGAGGCAATTCCTCCGTGTCTGACGGGATAGTTCTGCGGTGCTGTCGCACGAAGGAGTACGCCCGAACCAGGTTTCAAGAGGCTGTGATCTCCGTCAACATTATAAACCACCGTTGCTCGTCAGGTAATCGGAGGGGTGCGAGACAGATTTGTTCGAAGGGGAGATCCCTCGATCCACGCCCAAGATGCCGTTTGATTACCGCGTAACGGACGTCAACGAGGAATCGGTTCGAGCGAGGTTGGTTGAGTGAACCGTCCGCAACCCTACTTACTACTGATGTTGGTACCATCGTGTGCGCCGATTGGATCGGAGGATCTTCACTAGTGAAAAGGCGTTCATGGTGTGGGAGCCGGACTGCAGTATGGCTTGCTTAGACTCTACGGGGGCCATTATTATTGCAGAGTAGTTTGACTTATGAGGTGCACGAGCTTCTACGAGCTGCTTCCTACTGACCAGAGAGGGTACCTATGCGGCAATGAGTAGTACCCATAAAATGTGGAGACCCGAACCTGTCGTATTAAATCCTCTATTAATTAGGGAACTGCGTAGCAGCCGCAAGCGCCAATTCGGCTGAAAATGGAGCCCGGCACGGACATGTGCGTTATAAGGGCCATATAAGTACAGTATTTGCTGCAGATCTAAGCTACAGGCTTGCCTGGGACTGTACGGAACGTAGTTCAGGCAGTTGCTTACTATAAGCAACCCCCATGACAGCCCGCTCACCATGGTTGGCTAATCCCATTATAGCTTCTTATTGCAATACGTCGTGGTAAGCGTGAGCACGCATATGACGAGGGCATGTAGGCCGGTCGCCGGCGAGAACTTGTAATGGATAGGTCTTGAGTCTTAACTTATCCGAACTGCTTGGGAGCGGTGGTCAGACGTTATATACATGTTTCCAGTCACCAATCTTGAATCGTTCCCGAAAGATGTGGCTAGGCGCTCAGGCCGTGCGGGCCAGAATGAGACCAGCAACGATGGTTCTGTATCAGCATGTCTCTTCCAATGGCCCGCTACTGTATAGATCGAGCACTCTTTATCGAGTAATCTAGTTTGATACAGGATGAAACTACTGACCGCAGGCGCAATGCGCGTGGTCCGTCAAGCAGTGGGGCCGCTAACGACAGTAGTAGAGGGCGATAAGCCGTTCAGTTTCTACAAACAGTGGTTTCAGAGGCTTAATCGAGTACCACGAGGGAATTTCTTGGATGGTAAGGAACCATCAGCAACCGAGGGCCCTCTAAGTGAGTTATACTTCTAAGAGACTACGGGGGATACATAGCATTCTAGTGATACCACGAGAGCGGCGTGTTATACTAATCTGGTATTATACTAAAATAGGGCCCTGCGATAGGTTTATTACCTCCTGCACCTGGCACTGGCTGAATAAAGGACGGGCGCACAACCTTCTGATGCGGGTGTCACACTAGTCTTGCAGGTTTTATGATGCCGCCCGTACCGTCCCATAGGCGAATTATACTTCTGCCCTTGTCGTCTGAATGCGTGGCTAGGCAATTTCTAATCGAATAGTATCCGCTGTCGACTGAGCAACATTCATGCTTCCGGATATAACGAAGAAATAGATATTTCAATCGATGTTTCTAATGAGCTAGCTCGGGGCTTACCTTCTCGCTGCTCCTTCATGAAGCTCCTTGACCGGTGGCATCACTCTGGTTATACTCCACACTCTGCATCTGGGGAGCACCTTAGTCGAACTTCAGGTTTTGATTGACCGCACTTTATATGGGATAACGACTACCCGAGAATCTCCGTGTCAAGATGCACTAGCAGAGGAAGAGGGCAAAAGTCCTTTCCGAAAATCCCCAGGTAGTCGCCGGATACGACAAGGCCTAGACATTTCCCGCCCTCGTGCGCGATCGGATCTGTACCCATCCTATGTGTTGCGGGAGCAATTTAAACCTAACATAATATTCCAGGAAAGAGACCCTGGCTCATGAATGCTTTAATGTGAATGTAATCGACCTCGACACGCCCGTAGTCAACCTACCGTAAGACCCTCACGTACACAGACATCAAAAGGATATTAAGATCTGAATCTACATATCCTTAACGTTAGCTCTCTCAACGTATACGATAGAGGTAGACTGGTTTCTTCGAGGCGACTCGGCCGGGAGCGTTTATTTGACGAACGGTATCATGATGCCTTTGCCGTACCTTGATTGGGTGGATATCTGCGTGGGCAAGCATACAGCTGCGTCCGGAGTCCATGTTAACGCGGGATGCAATGTAATTTGATATTGCACTTGCGGAGGCCGTTTTGTCAAAAAAACAAGAGGGTTAGGTGACTTGTATTAGCACATAGACTGGTTTACGATCTACCTGACCACGTTGGAATAAACGTCTTTTTGTAGCCCCGCTGTGCGCGATCGTATGATATCCAGGTCACGGCGATGGCACATGCTCGGTAGCGTAAGGAGGCTGTTGACTAACAGTGGCATCAGACCACGAGAGAACAGCATACTACGAGGCCAGCCGTTAATGTTAATGCACAGGCTTGACAGCGTTTGAGAGGCCGGTGACTGCTTCCGCATGGAGCCTGCGGTGTAGTGCTAACCGCACCTAGGAAAGCAACTACAATCGAAATAGATGAGTACTTCGTCAACACTCTAGTAATGGGGTTCCCGGGCATCAATTGTTAAAATCGTTTGCAAGGCGTTAGCGACCACACATACTTTTCAAGTCGGCATATATATGAAGCTAGGAAGGTCGCGTTTTATTAAGCTGCGCTCTATCTGGCCTCTTGTAGCTAATAACTCCTTTCGAAGCAAGGAACTTCTATTCCTATCGCATTAGGATCGTCTGGACATTGCCAGTATCTGCGATATAGCCCTTCATTGTGCCCCCATTGCTTAGATTTCAAACGGGTCTTGGAAAAACCGACCCTATTTCAAGACCACGTCCCATCCGTTTAAATTTGGGTGTCCGGCGCTCCTGCGATGTACTACTCGCACCGAGGGACCGTGGGGACTGGTTCACACGAAGTGTTACCGGACGACGAGCCTAATACAGCGTCGGTGCACGTTTTTGTTGCTACAGCTGTGATCGGCTTATTCATCACTATCATGAGTTGTACAAGGGGTTCGGAAACGATACGTGCATGGTCGCGCGACCTCCACGACGTCAACGATTATGAGCTAAGAGTTGGGTAGCACCGACGATGAGTACCGTCCAACATGAAAACTCGCGGCCTGGGTGACAGTGTGTGGCCGTATGCCTAGGCCGGCAAACAGGCGTTTGCTACATCCCGAGGCGAGCCCTTCCTCCGTGATGCGCGCCTAACAATTCATATCAAGGTGGCTCTCAAAGCTAAGGGATGTGTGCGCAGGATAGGGATTTGCGGCTGTTGGGCGATTTCATACTATTTGGTTTTAACCGTTGAGTGCGTATTTTTCCGAAGTCATATTTAAAGGCGCGATCTAGCCTAGGCATTAACGCTGCGCTGAGCTCCCCCCGAGAATATGGAACCCCGCGCCCCTACTTACGAAAACGCCATTATCCTAATTTTTAGATATGATACAGTGTGCGGGTATTTCAAGGTTGTTAGCTGCAGCCAAGACAGCTTCATGACGGGATGGTAGAGATGATACGAACAGCCCTCCGTTCCCCAACCGGCATGGCTCCACGAGTTTGTATCAGTGGTCCACTGCTTCAATTCAAATTGTTGGTGGATTTGCCCTTATCCTCAGTTTCCTCTTTAACCCAGGTAGCTACTGAATAAAGCAGATCAGTAAAAAAAAGGACCGGTACACCATTATAGTGGGGTAAACACAGCTCGGGTCGCACCTTAGGTGGACCGCGATGGAGTCGGGCCTGCCCATGTTAGGTTCTCAGTTGACAGTTTAAAATCCATTTGTTCATTTGTGGATTGTGTACCGTCCTAAGGGTGACCAAGGTACAACCAGGCTTGGGTGTCAGCGATGACCTAATCCTCGGACGTAGGGAACTCGACCTTGCAATCCCTTGGGGCTCGGAGCTCAGGTTCCGTGCCTTTGGATGGCAGAGTGCCTGACGTGCACCGGCATCTAAGTCAGCACCGATCCTCTAGGACCGCCGCGCGCTTTCCGTATTCTCTTAATTCGTCTAATAAGAAACAGATGGGTCTTAGAACATGGAAAAGGAAAGCTGTCGGAGAACGACGACTATCCTCTAACATGTGTTAAATTGGCATGCTGCCTGTCGTGGAAGTATCCCTGCGCCTGATCTCGTCGTGCCACCCCGGCGCGAATTATCTGTGCCGTAATGCACCGAACAAAACCGTATGTAACGGAAATTTAAATTCCCGAGTTTACTAGACTTTTCTCGAGATACTCTTTCCTCTCCCACCCTGCGGACCGGTGTGCAGACGGCCCCGTTTTCAGACCGGAGAGTCAAGCGCTGTCTCCACGGGGTTAGTGACTGATTGAAACTATAGAATCCCCGAGTAAACTAGCCTTGCCATGTCGAATCATAGGACGGCCTCCCCCATTGGAATCTGCCGTTATAGACTTACACCTGGGCATCGGGGTTAAAACCCACTGGTTCCCAAGCTCAGTGACGCCGGTGCAACTTCTGAAAACAGCAGGTGGGGGTTCCCTCTCGAACTAAGCCGGGCAGTTAGCCGGATGAGGAATCATTGAGTATAGAGACTAACCCCATCCGACTCCATCTAATAGACAGTCCCCTCTTTCAACCTCGTTTCCGTGCGGTCTAGGCAGCTTGGTGATATACCGATGGCCTTTTAATGCTGCACACATTAGATCGCCGCACAGAGGGCTGCTGGTATCCTAGTATGTGGGACACTAAGACTACGGCCCGGTCTGCCAAGGTCAGGGTATGTACACGCTTTCGCACTACCAATGCTACAGCAGGGGAATAATGCGAGACTTTGAGCGAACTTTTGACATTTAAGTTCTAATGACAGCGACTTGTGCCCTCCAGTCCATACCTATGGCCGAATGGATCTTTTCTGGCCTCATATGCGTCTTGGTTCCGGACCAATGATTACCGATTGAACGCGAGGTGACATATCGTCGCCTTGGCGCTGTTCAGTTGCTCCACTGGCGCGCTGACCGGCACACTTCTTGCCGATACTTTTGAAATAGATAATCTAGGTTACGATTCCAGCCGTCATCCAGGGTTTTCTATGATCTACAGCGGGCCCAACCATTGCGGGAAGATGTACAGTGAAGCTTCATGCCTATGTCGGTTATCTTATCGTTCAATACGTGCCGCGGTTGCCGAATAGTCAGCGCTAAGGGCCGTGACACGCCTGTTACTCAATAGTAGGTCTCTCTGTTTTTGTGTCGCTGCCCCCAACTTCACTTAGGACAGAAGCCTACCTTGATAGGAGTCCGTCCCATCTAGCAATGCTGCGAGGGAGTATAGATGACTCACGTCCGTAGCTATCCGGATGGTCCACATTAGTATATCGTACCGAGCGCGTTGTGCGCCTTATGGCTGGGCAGGTCCTCCAATTATTCAATCTATAGATCCTTACCCCAGTTGGTAGATACATAGACACTT"))
