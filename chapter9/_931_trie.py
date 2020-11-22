from reprlib import recursive_repr
from copy import deepcopy

class Node():

    def __init__(self, value = None, children = {}):
        self.__value = value
        self.__children = children

    @recursive_repr()
    def __repr__(self):
        if self.children == {}:
            return ""
        else:
            string = ""

            for weight, child in self.children.items():
                string += str(self.__value) + '->' + str(child.__value) + ':' + str(weight) + '\n'            
                string += repr(child) 
            return string


    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, children):
        self.__children = children

    
    def isLeaf(self):
        if self.__children == {}:
            return True
        else:
            return False


def trieConstruction(patterns):
    rootNode = Node(value=0)
    nodeCount = 1
    
    for pattern in patterns:
        currentNode = rootNode
        for symbol in pattern:
            if symbol in currentNode.children:
                currentNode = currentNode.children[symbol]
            else:       
                newNode = Node(value=nodeCount, children={})
                currentNode.children[symbol] = deepcopy(newNode)
                currentNode = currentNode.children[symbol]
                nodeCount += 1
    
    return rootNode
    


if __name__ == "__main__":
    
    file =  open('data/trie.txt', 'r')

    patterns = [line.rstrip('\n') for line in file.readlines()]

    print(trieConstruction(patterns))