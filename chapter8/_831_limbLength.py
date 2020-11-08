import numpy as np
import ast

def limbLength(n, j, matrix):
    length = float('inf')

    for i in range(n-1):
        for k in range(i+1, n):
            if i != j and k != j:
                limb_length_j = (matrix[i,j] + matrix[j,k] - matrix[i,k])/2
                if limb_length_j < length:
                    length = limb_length_j
            
    return int(length)


if __name__ == "__main__":
    
    file = open('data/limbLength.txt', 'r')

    n =  int(file.readline().rstrip('\n'))
    j =  int(file.readline().rstrip('\n'))


    matrix = np.array([[int(i) for i in line.split(' ')] for line in file])
    
    print(limbLength(n,j,matrix))