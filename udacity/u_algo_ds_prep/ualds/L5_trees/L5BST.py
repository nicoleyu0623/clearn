class BST:

    class _Node:
        def __init__(self,value):
            self._value = value
            self._left = None
            self._right = None

    def __init__(self,value):
        self._root = self._Node(value)


    def print_tree(self):
        traversal = ''
        traversal = self.preorder_print(self._root, traversal)

        traversal = ''.join(list(traversal)[0:len(traversal)-1])
        return traversal

    def preorder_print(self, currentNode, traversal):
        if currentNode is None:
            return traversal
        else:
            traversal += str(currentNode._value) + '-'
        traversal = self.preorder_print(currentNode._left, traversal)
        traversal = self.preorder_print(currentNode._right, traversal)
        return traversal

    def insert(self,value):
        self.insert_bst(self._root, value)

    def insert_bst(self, node, value,):
        if value < node._value :
            if node._left:
                self.insert_bst(node._left, value)
            else:
                node._left = self._Node(value)
        else:
            if node._right:
                self.insert_bst(node._right, value)
            else:
                node._right = self._Node(value)


    def search(self,value):
        return self.search_bst(self._root, value)

    def search_bst(self, node, value):
        if node is None:
            return False
        if value < node._value:
            if node._left:
                self.search_bst(node._left, value)
        elif value > node._value:
            if node._right:
                self.search_bst(node._right, value)
        else:                   #value = node._value
            return True
        return False

#--------- teststing --------#

def testBstInsertSearch():

    #setup
    tree = BST(4)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    print(tree.print_tree())

    # Check search
    # Should be True
    print(tree.search(4))
    #should be false
    print(tree.search(6))

def main():
    testBstInsertSearch()

if __name__ == '__main__':
        main()
