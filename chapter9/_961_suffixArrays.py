

def suffixArray(text):
    suffixes = []

    for i in range(len(text)):
        suffixes.append((i,text[i:]))
    
    suffixes.sort(key = lambda x: x[1])

    return list(map(lambda x: x[0], suffixes))


if __name__ == "__main__":
    
    file = open('data/suffixArrays.txt', 'r')

    text = file.readline().rstrip('\n')

    suffixes = suffixArray(text)
    print(str(suffixes)[1:-1])