def pathToGenome(path):
    # Input: A sequence path of k-mers Pattern_1, … ,Pattern_n such that the last k - 1 symbols of Pattern_i are equal to the first k-1 symbols of Pattern_i+1 for 1 ≤ i ≤ n-1.
    # Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Pattern_i (for 1 ≤ i ≤ n).

    text = path[0]
    for i in range(1,len(path)):
        if path[i-1][1:] == path[i][:-1]:
            text += path[i][-1]
        else:
            return ""
    return text


if __name__ == "__main__":

    file = open("data/pathToGenome.txt", 'r')
    path = [line.rstrip('\n') for line in file]


  
    print(pathToGenome(path))