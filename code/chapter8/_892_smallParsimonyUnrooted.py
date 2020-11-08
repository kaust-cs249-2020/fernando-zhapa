from _891_smallParsimony import Node, smallParsimony, hammingDistance
from math import ceil
from reprlib import recursive_repr
from copy import deepcopy

class NodeU(Node):

    def __init__(self, label=None, score =0, daughter=None, son=None, tag = False, value = -1):
        super().__init__(label, score, daughter, son, tag, value) 

    # @recursive_repr()
    # def __repr__(self):
    #     if self.isLeaf():
    #         return str(self.value) + ':'+ str(self.tag) + ':' + str(self.label) + ':' + str(self.score) + '\n'
    #     else:
    #         string = ""

    #         string += str(self.value) + ':'+ str(self.tag) + ':' + self.label + ':' + str(self.score) + '->'  + '\n'
    #         string += str(self.value) + '->' +  '\n'
    #         string += str(self.daughter)
    #         string += str(self.son)
    #         return string

    @recursive_repr()
    def __repr__(self):
        if self.isLeaf():
            return ""
        
        elif self.label == 'ROOT':
            string = ''
            daughter = self.daughter
            son = self.son
            weight = hammingDistance(son.label, daughter.label)
            
            string += str(son.label) + '->' + str(daughter.label) + ':' + str(weight) + '\n'
            string += str(daughter.label) + '->' + str(son.label) + ':' + str(weight) + '\n'

          
            string += str(daughter)
            string += str(son) 

            return string
        else:
            string = ""        
            if self.daughter != None:
                daughter = self.daughter
                weightDau = hammingDistance(self.label, daughter.label)
                
                string += str(self.label) + '->' + str(daughter.label) + ':' + str(weightDau) + '\n'
                string += str(daughter.label) + '->' + str(self.label) + ':' + str(weightDau) + '\n'

                son = self.son
                weightSon = hammingDistance(self.label, son.label)
                string += str(self.label) + '->' + str(son.label) + ':' + str(weightSon) + '\n'
                string += str(son.label) + '->' + str(self.label) + ':' + str(weightSon) + '\n'

                string += str(daughter)
                string += str(son) 

            return string

    @property
    def label(self):
        return super().label

    @label.setter
    def label(self, label):
        super(NodeU, self.__class__).label.fset(self, label)
    
    @property
    def tag(self):
        return super().tag

    @tag.setter
    def tag(self, tag):
        super(NodeU, self.__class__).tag.fset(self, tag)


    @property
    def daughter(self):
        return super().daughter

    @daughter.setter
    def daughter(self, daughter):
        super(NodeU, self.__class__).daughter.fset(self, daughter)
    
    @property
    def son(self):
        return super().son

    @son.setter
    def son(self, son):
        super(NodeU, self.__class__).son.fset(self, son)

    @property
    def score(self):
        return super().score

    @score.setter
    def score(self, score):
        super(NodeU, self.__class__).score.fset(self, score)
    

    @property
    def value(self):
        return super().value

    @value.setter
    def value(self, value):
        super(NodeU, self.__class__).value.fset(self, value)

def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def restartTags(tree):
    tree = deepcopy(tree)
    if tree != None:
        if not tree.isLeaf():
            tree.tag = False
            if tree.label != 'ROOT':
                tree.label = None
            tree.score = 0
            tree.daughter = restartTags(tree.daughter)
            tree.son = restartTags(tree.son)
        else:
            tree.tag = False
            tree.score = None
    return tree

# O(2n)
def buildTree(adjList, num_leaves):
    nodes = {}

    idx = 0

    # O(n) assign only leaves
    while idx<num_leaves:
        for i in range(len(adjList)):
            x, y = adjList[i]
            
            if isInt(x) and not isInt(y):
                value = int(x)
                valueLeaf = 2*(value - num_leaves)

                if value in nodes:
                    nodeLeaf =  NodeU(label=y, value = valueLeaf+1)

                    nodes[value].son = nodeLeaf
                else:
                    nodeLeaf =  NodeU(label=y, value = valueLeaf)
                    node = NodeU(value = value, daughter=nodeLeaf)
                    nodes[value] = node

                adjList.remove((x,y))
                adjList.remove((y,x))

                idx += 1
                break    
            
        
    # O(n) assign internal nodes
    while bool(adjList):
        for i in range(len(adjList)):
        
            x, y = adjList[i]
            x, y = int(x), int(y)

            if x > y:

                if x in nodes:

                    if y in nodes and nodes[x].son == None:
                        nodes[x].son = nodes[y]

                        del nodes[y]
                
                else:
                    if y in nodes:
                        parent = NodeU(value=x, daughter=nodes[y])

                        nodes[x] = parent
                        del nodes[y]

                adjList.remove((str(x),str(y)))
                adjList.remove((str(y),str(x)))

                break    

    return nodes            

# 0(m*n^2)
def smallParsimonyUnrooted(subtrees, m):
    subtrees =  list(subtrees.items())

    val1, subtree1 =  subtrees[0]
    val2, subtree2 =  subtrees[1]

    rootValue =  max(val1, val2) + 1

    root = NodeU(value=rootValue, daughter=subtree1, son = subtree2)

    # O(n)
    root = restartTags(root) #useful for interchange heuristic problem

    # 0(m*n^2)
    tree = smallParsimony(root, m)

    tree.label =  'ROOT'

    return tree



if __name__ == "__main__":
    
    file =  open('data/smallParsimonyUnrooted.txt', 'r')

    n = int(file.readline().rstrip('\n'))
    
    edges =  [tuple(line.rstrip('\n').split('->')) for line in file]
    m = len(edges[0][0])
    
    nodes = {}
   
    nodes =  buildTree(edges, n)


    tree = smallParsimonyUnrooted(nodes, m)


    score =  tree.totalScore()

    print(score)
    print(tree)


