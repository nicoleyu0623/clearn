'''
specs:
Deque()  starts as empty
addFront(item)
addRear(item)
removeFront(item)
removeRear(item)
isEmpty()
size()
'''


class Deque(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

    def addFront(self, item):
        self.items.append(item) ##items will be reversed

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop() #actually stored as a last el in array

    def removeRear(self):
        return self.items.pop(0)  # removes element at index 0

    def __repr__(self):
        return repr(self.items)

from pprint import pprint as pp
if __name__ == '__main__':
    d = Deque()
    d.addFront('hello')
    d.addFront('my')
    d.addRear('world')
    d.addRear('beautiful')
    pp(d)
    x = d.removeFront()
    pp(d)
    pp(d.size())