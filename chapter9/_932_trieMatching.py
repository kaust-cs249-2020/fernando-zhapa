from _931_trie import trieConstruction, Node


def prefixTrieMatching(text, tree):
   
    i = 0
    while not tree.isLeaf() and i < len(text):
        symbol = text[i]
        if symbol in tree.children:
            tree = tree.children[symbol]
            i += 1
        else:
            return False
    
    if tree.isLeaf():
        return True
    else:
        return False
def trieMatching(text, patterns):
    tree = trieConstruction(patterns)
    positions = []
    for i in range(len(text)):
        suffix = text[i:]
        if prefixTrieMatching(suffix, tree):
            positions.append(i)
    
    return positions


if __name__ == "__main__":
    
    file = open('data/trieMatching.txt', 'r')

    text = file.readline().rstrip('\n')

    patterns = [line.rstrip('\n') for line in file.readlines()]

    positions = trieMatching(text, patterns)

    toPrint = ''

    for item in positions:
        toPrint += ' ' + str(item)

    print(toPrint)