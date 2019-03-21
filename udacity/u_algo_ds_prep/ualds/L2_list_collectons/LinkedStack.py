import unittest

import Empty
import copy



class LinkedStack:
    """LIFO stack iplementation using a sngly linked list for storage"""
    #---------------nested class ----------------------------------------
    class _Node:
        def __init__(self,element, next=None):
            self._element = element
            self._next = next

    #----------------- stack methods ------------------------------------

    def __init__(self):
        """create emtpy stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """return number of elements in the stack"""
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, el):
        "add element to the top of the stack"

        self._head = self._Node(el, self._head)
        self._size += 1

    def top(self):
        """return a head element without modifying the list
            return error if list is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element


    def pop(self):
        "remove the first element from the list"
        if self.is_empty():
            raise Empty("stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


#------------ testing class LinkedStack ---------------
class  LinkedStackTest(unittest.TestCase):
    """unit tests for LinkedStack"""

    def setUp(self):
        self._stack_e0 = LinkedStack()
        self._stack_e1 = LinkedStack()
        self._stack_e1.push("one")
        self._stack_e2 = LinkedStack()
        self._stack_e2.push("one")
        self._stack_e2.push("two")


    def tearDown(self):
        pass

    def test_emptyStack(self):
        """check empty stack"""
        lst = self._stack_e0
        self.assertEqual(len(lst),0)

    def test_pushing(self):
        lst = copy.deepcopy(self._stack_e0)
        lst.push("one")
        self.assertEqual(len(lst), 1)
        self.assertEqual(lst._head._element, "one")
        lst.push("two")
        self.assertEqual(lst._head._element, "two")

    def test_top(self):
        self.assertEqual(self._stack_e1.top(), "one")

    def test_pop(self):
        lst = copy.deepcopy(self._stack_e2)
        res = lst.pop()
        self.assertEqual(res, "two")
        self.assertEqual(len(lst),1)

if __name__ == '__main__':
    #unittest.main()
    main()