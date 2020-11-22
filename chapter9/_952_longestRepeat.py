from _951_suffixTree import modifiedSuffixTrieConstruction, Node

def longestRepeat(tree, text, currString = "", longestString = ""):


    if len(tree.children) > 1:
        for _, child in tree.children.items():
     
            if len(child.children) > 1:
                start = child.position
                length = child.length
                candidateStr = currString + text[start:start+length+1]
                longestString = max([candidateStr, currString, longestString], key=len)
                longestString = max([longestRepeat(child,text,candidateStr, longestString), longestString], key=len)
    else:
        longestString = ''

    return longestString


if __name__ == "__main__":
    
    file = open('data/longestRepeat.txt', 'r')

    text = file.readline().rstrip('\n') + '$'

    tree = modifiedSuffixTrieConstruction(text)

    tree.shrinkTrie(0)

    tree.length = -1
    tree.position = 0

    longest = longestRepeat(tree, text)

    print(longest)