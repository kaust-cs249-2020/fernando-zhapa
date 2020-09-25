def printListOfTuples(list):
    string = ""
    for item in list:
        string += '('+item[0]+'|'+item[1]+') '
    print (string[:-1])

def k_d_composition(k, d, string):
    #returns the k-d composition of the text. k-d composition are pairs of k-mers separated by distance d
    composition = []
    for i in range(len(string) - (2*k + d) +1):
        firstKmer = string[i:i+k]
        secondKmer = string[i+k+d:i+2*k+d]
        composition.append((firstKmer,secondKmer))
        composition.sort()
    return composition


if __name__ == "__main__":
    printListOfTuples(k_d_composition(3,2,"TAATGGGATGCCATGTT"))