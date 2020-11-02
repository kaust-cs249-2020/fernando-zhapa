class Node():
    def __init__(self, value, parent=None):
        self._value = value
        self._parent = parent #is a tuple that contains parent value and weight
        self._children = []
    
    def __repr__(self):
        return "Node: " + str(self._value) + "\tParent: " + str(self._parent) + "\tChildren: " + str(self._children) + '\n'

    def insertChild(self, child, weight):
        self._children.append((child,weight))

    def getParent(self):
        return self._parent
    
    def setParent(self, parent, weight):
        self._parent = (parent, weight)
    

    def maxNode(self):
        # returns the maximum node value found
        if self._parent != None:
            parent, _ =  self._parent
            maximum = parent
        else:
            maximum = float('-inf')

        for node, _ in self._children:
            if node > maximum:
                maximum = node
        return maximum

    def dropConnection(self, node):

        if  self._parent != None:
            parent, _ =  self._parent
        else:
            parent = -1

        if node == parent:
            self._parent = None
            where = 'parent'
        else:
            toRemove = None
            for child, weight in self._children:
                if child == node:
                    toRemove = (child, weight)
                    break
            self._children.remove(toRemove)
            where = 'children'
        return where
    
    def addConnection(self, node, weight):
        if  self._parent == None:
             self._parent = (node, weight)
        else:
            for child, _ in self._children:
                if child == node:
                    child.append((node, weight))
                    break

    def adjacencyListString(self):
        if self._parent != None:
            parentVal, weight = self._parent
            string = str(self._value) + '->' + str(parentVal) + ":" + str(weight) + '\n'
        else:
            string = ""

        for nodeVal, weight in self._children:
            string += str(self._value) + '->' + str(nodeVal) + ":" + str(weight) + '\n'
        
        return string