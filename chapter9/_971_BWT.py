import numpy as np
def BWT(text):
    strings = []

    currString = text

    for i in range(len(currString)):
        strings.append([char for char in currString])
        currString = currString[1:] + currString[0]

    strings.sort()

    strings = np.array(strings)

    return ''.join(strings[:,-1])


if __name__ == "__main__":
    
    file = open('data/BWT.txt', 'r')

    text = file.readline()

    print(BWT(text))