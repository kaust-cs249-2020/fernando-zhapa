

def recursiveSharedKmers(k, string1, string2, idx2):
    kmers = []

    if len(string1)==1 or len(string2) ==0:
        return []
    for i in range(len(string1)-k+1):
        if isSharedKmer(string1[i:i+k], string2[i:i+k]):
            kmers.append((i,i+idx2))

    kmers += recursiveSharedKmers(k, string1[:-1], string2[1:], idx2+1)

    return kmers


def reverseComplement(string):
    complements = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}
    revComplem = ""
    for char in string:
        revComplem = complements[char] + revComplem
    return revComplem

def isSharedKmer(str1, str2):

    if str1 == str2:
        return True
    elif reverseComplement(str1) == str2:
        return True
    else:
        return False

def sharedKmers(k, string1, string2):
    
    kmers = recursiveSharedKmers(k, string1, string2,0)
    kmers2 = recursiveSharedKmers(k, string2, string1,0)
    kmers2 = [(i,j) for j,i in kmers2]
    return set(kmers + kmers2)


if __name__ == "__main__":
    
    file = open('data/sharedKmers.txt', 'r')

    k = int(file.readline())

    string1 = file.readline().rstrip('\n')
    string2 = file.readline().rstrip('\n')

    print(sharedKmers(k, string1, string2))