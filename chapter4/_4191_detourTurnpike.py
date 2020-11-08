import sys
sys.path.append('..')

from lib import spacedPrint
from math import sqrt


def turnpike(differences):
    sizeOriginal = int(sqrt(len(differences)))

    start = int((sizeOriginal)*(sizeOriginal-1)/2)

    original = []

    while start < len(differences):
        original.append(differences[start])
        start += sizeOriginal
        sizeOriginal -= 1
    return original

if __name__ == "__main__":
    
    file = open('data/turnpike.txt','r')

    diffs = [int(i) for i in file.readline().rstrip('\n').split(' ')]

    spacedPrint(turnpike(diffs))
