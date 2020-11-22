from copy import deepcopy
from reprlib import recursive_repr
import sys
sys.setrecursionlimit(5000)


class Node():

    def __init__(self, position = None, symbol = None, startPos =  None, length = None, children = {}):
        self.__position = position
        self.__symbol   = symbol
        # self.__startPos = startPos  #used in trie
        self.__length   = length    # used in tree
        self.__children = children


    @recursive_repr()
    def __repr__(self):
        if self.children == {}:
            return ""
        else:
            string = ""

            for symbol, child in self.children.items():
                string += str(self.__symbol) + '->' + str(child.__symbol) + ':' + str(child.__position)+ '\n'            
                string += repr(child) 
            return string

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, children):
        self.__children = children
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol):
        self.__symbol = symbol

    
    def isLeaf(self):
        if self.__children == {}:
            return True
        else:
            return False


    def shrinkTrie(self, length):

        if len(self.children) > 1:
            for _, child in self.children.items():
                child.__length = 1
                child.shrinkTrie(1)

        elif len(self.children) == 1:
            _, onlyChild = list(self.children.items())[0]
            
            self.children = onlyChild.children
            length+=1
            self.length = length 
            self.shrinkTrie(length)

        

    def printTree(self, text):
        
        if self.children != {}:
            for _, child in self.children.items():
                # print(child.__position, child.__length)
                # print(child)
                start = child.__position
                length = child.__length
                print(text[start:start+length], start, length, descent)
                child.printTree(text)
       

# ModifiedSuffixTrieConstruction(Text)
#         Trie ← a graph consisting of a single node root
#         for i ← 0 to |Text| - 1
#             currentNode ← root
#             for j ← i to |Text| - 1
#                 currentSymbol ← j-th symbol of Text
#                 if there is an outgoing edge from currentNode labeled by currentSymbol
#                     currentNode ← ending node of this edge
#                 else
#                     add a new node newNode to Trie
#                     add an edge newEdge connecting currentNode to newNode in Trie
#                     Symbol(newEdge) ← currentSymbol
#                     Position(newEdge) ← j
#                     currentNode ← newNode
#             if currentNode is a leaf in Trie
#                 assign label i to this leaf
#         return Trie


def modifiedSuffixTrieConstruction(text):
    rootNode = Node()
    
    for i in range(len(text)):
        currentNode = rootNode
        for j in range(i,len(text)):
            symbol = text[j]
            if symbol in currentNode.children:
                currentNode = currentNode.children[symbol]
            else:       
                newNode = Node(position= j, symbol= symbol, children={})
                currentNode.children[symbol] = deepcopy(newNode)
                currentNode = currentNode.children[symbol]

        # if currentNode.isLeaf():
        #     currentNode.position = i
    return rootNode


# ModifiedSuffixTreeConstruction(Text)
#     Trie ← ModifiedSuffixTrieConstruction
#     for each non-branching path Path in Trie
#         substitute Path by a single edge e connecting the first and last nodes of Path
#         Position(e) ← Position(first edge of Path)
#         Length(e) ← number of edges of Path
#     return Trie

# def modifiedSuffixTreeConstruction(text):
#     trie = modifiedSuffixTrieConstruction(text)

#     trie.shrinkTrie(0)



if __name__ == "__main__":
    
    file = open('data/suffixTree.txt', 'r')

    text = file.readline().rstrip('\n')

    trie = modifiedSuffixTrieConstruction(text)

    trie.shrinkTrie(0)

    trie.printTree(text)
