
import Empty
import unittest
import copy

class LinkedQueue:
    """FIFO  queue iplementation using a sngly linked list for storage
        GTGb
    """
    #---------------nested class ----------------------------------------
    class _Node:
        def __init__(self,element, next=None):
            self._element = element
            self._next = next

    #----------------- stack methods ------------------------------------

    def __init__(self):

        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """return a head element without modifying the list
            return error if list is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element

    def dequeue(self):
        """remove and return the first element of the queue"""

        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


    def printQ(self):
        if self.is_empty():
            print("empty queue")
        else:
            buf = "["
            current = self._head
            while current._next:
                buf += str(current._element) + ","
                current = current._next
            buf = ''.join(list(buf)[0:-1]) #strip off last ','
            buf += "]"
            print(buf)



