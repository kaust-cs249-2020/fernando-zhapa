import sys
sys.path.append("..")
from lib import spacedPrint

################################################
############## SKEW ############3

#gets all the values needed for the Skew diagram. This consists on the difference of 'G' and 'C' at a given point i of the string 
def skewDiagram(string):
    diffs = [0]*(len(string)+1)
    for i in range(1,len(string)+1):
        if string[i-1] == 'G':
            diffs[i] = diffs[i-1] + 1
        elif string[i-1] == 'C':
            diffs[i] = diffs[i-1] - 1
        else:
            diffs[i] = diffs[i-1]
    return diffs

# spacedPrint(skewDiagram("GAGCCACCGCGATA"))


def minimumSkew(string):
    skew = skewDiagram(string)
    minSkew = float('inf')
    minimums = []
    for i in skew:
        if i<minSkew:
            minSkew=i
    for i in range(len(skew)):
        if skew[i] == minSkew:
            minimums.append(i)
    return minimums

if __name__ == "__main__": 
    file_sk = open("data/dataset_369238_6.txt", "r")
    text_sk = file_sk.read()
    spacedPrint(minimumSkew(text_sk))
