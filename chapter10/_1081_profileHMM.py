import pandas as pd
import numpy as np

def generateTransitionHMM(num_cols):
    labels = ["S", "IO"]

    for i in range(num_cols):
        labels.append("M"+str(i+1))
        labels.append("D"+str(i+1))
        labels.append("I"+str(i+1))

    labels.append("E")

    size = len(labels)

    data = pd.DataFrame(data = np.zeros((size, size)), columns = labels, index = labels)

    return data


def cols_to_drop(alignment, threshold):
    rows = len(alignment)
    idx_to_drop = []
    for col in range(len(alignment[0]))
        null = [item for item in alignment[:,col] if item == '-']
        
        ratio = len(null)/rows
        if ratio >= threshold:
            idx_to_drop.append(ratio)
    return idx_to_drop

def processRow(row, transition):

    dropped =  cols_to_drop(alignment, threshold)
    for i in range(len(row)):
        if i in dropped:
            if i == 0               # if first column
                if row[i] != "-":
                    transition["S"]["IO"] += 1
                    prevState = "IO"
            else:
                if row[i] != "-"
                    nextState = getNext(prevState,'insert')
                    transition[prevState][nextState] += 1
                    prevState = nextState

        else:
            if i == 0               # if first column
                if row[i] != "-":
                    transition["S"]["M1"] += 1
                    prevState = "M1"
                else:
                    transition["S"]["D1"] += 1
                    prevState = "D1"
            else:
                if row[i] != "-"
                    nextState = getNext(prevState,'match')
                else:
                    nextState = getNext(prevState,'delete')
                    transition[prevState][nextState] += 1
                    prevState = nextState
                    
def processAlignment(alignment, threshold):
    dropped = cols_to_drop(alignment, threshold)

    transition = generateTransitionHMM(len(dropped))

    for row in alignment
        transition = processRow(alignment[row], transition)

    finalTransition = normalize(transition)

    return finalTransition



if __name__ == "__main__":

    file = open('data/profileHMM.txt')
    
    threshold = float(file.readline().rstrip('\n'))

    states = file.readline().rstrip('\n').split(' ')

    alignment = [line.rstrip('\n') for line in file.readlines()]

    print(generateTransitionHMM(2))

