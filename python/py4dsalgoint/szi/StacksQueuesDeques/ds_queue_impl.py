'''
Specs:
Queue() creates a new empty stack
enqueue(item) puts item on the top
dequeue() #removes item from the top
isEmpty()
size() return number of elements
'''

class Queue(object):
    def __init__(self):
        self.items=[]  #using list

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        el = self.items[0]
        self.items = self.items[1:]
        return el

    def enqueue_alt(self,item):
        self.items.insert(0,item)

    def dequeue_alt(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)

from pprint import pprint as pp
if __name__ == '__main__':
    q = Queue()
    pp(q.isEmpty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    pp(q)
    x=q.dequeue()
    pp('x:{} q:{}'.format(x,q))
    q1=Queue()
    q1.enqueue_alt('a')
    q1.enqueue_alt('b')
    q1.enqueue_alt('c')
    pp(q1)
    x=q1.dequeue_alt()
    pp('x:{} q1:{}'.format(x,q1))
