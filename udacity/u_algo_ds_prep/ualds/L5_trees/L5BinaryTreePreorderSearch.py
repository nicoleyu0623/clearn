class BinaryTree:

    class _Node:
        def __init__(self,value):
            self._value = value
            self._left = None
            self._right = None


    def __init__(self,value):
        self._root = self._Node(value)


    def search(self, find_value):
        """Return True if the value is in the tree, return
        False otherwise."""
        return self.preorder_search(self._root,find_value)

    def preorder_search(self, currentNode, find_value):
        #print('at node {0}'.format(currentNode._value))
        if currentNode is None:
            return False
        elif currentNode._value == find_value:
            return True
        else:
            return self.preorder_search(currentNode._left,find_value) or\
                   self.preorder_search(currentNode._right,find_value)
        return False

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

#--------- teststing --------#

def testBinaryTreePreorderSearch():

    #setup
    tree = BinaryTree(1)
    tree._root._left = tree._Node(2)
    tree._root._right = tree._Node(3)
    tree._root._left._left = tree._Node(4)
    tree._root._left._right = tree._Node(5)

    # Test search
    # Should be True
    print(tree.search(3))
    # Should be False
    print(tree.search(6))

    # Should be 1-2-4-5-3
    print(tree.print_tree())

def main():
    testBinaryTreePreorderSearch()

if __name__ == '__main__':
        main()