from _953_longestSharedSubstring import ColoredNode, modifiedSuffixTrieConstruction



if __name__ == "__main__":
        
    file = open('data/shortestNonShared.txt', 'r')

    str1 = file.readline().rstrip('\n')
    str2 = file.readline().rstrip('\n')

    wholeText = str1 + '#' + str2 + '$'

    tree = modifiedSuffixTrieConstruction(wholeText)

    tree.symbol = "ROOT"
    tree.shrinkTrie(0)

    tree.coloringTree(len(str1)+1)

    shared = tree.shallowestNonPurpleNode(wholeText)

    print(shared)