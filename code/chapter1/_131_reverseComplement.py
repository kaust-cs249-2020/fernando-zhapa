
#########################################
############ REVERSE COMPLEMENT #########

#given an ADN strand, returns its reverse complement
def reverseComplement(string):
    complements = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}
    revComplem = ""
    for char in string:
        revComplem = complements[char] + revComplem
    return revComplem

if __name__ == "__main__": 
    text_rc = "CACAGCTAAGAGATAGCTGTTGCCACCCCTATCACGGCTTGTTTCTCGTGTTGCGGGCCACGTTATGTCGCTTCTTGTAAAGGCCGCTGTAGACGGGAACCAAATCTAAATGTACGGTTACGCTACGAGACTCAAAATCCTGCCTGGCAGAATCGT"
    print(reverseComplement(text_rc))
