'''
Doubly linked list refernces both next and previous  elements
One can traverse such list from head to tail and from tail to head

we can implement
push()
append()
pop()
pop_rear()
size()
'''


class DlNode(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, item):
        nnode = DlNode(item)

        if not self.head:     #empty dbl linked list
            self.head = self.tail = nnode
        else:
            ohead = self.head
            ohead.prev = nnode
            nnode.next = ohead
            self.head = nnode

        self.length +=1
        if self.length == 2:
            self.tail = self.head.next
            self.tail.prev = self.head

    def pop(self):
        if not self.head:  #empty list
            return None
        item = self.head.value
        self.head = self.head.next
        self.length -=1
        return item

    def __repr__(self):
        s = '[]'
        if self.length == 0:
            return s
        else:
            s='['
            cnode = self.head
            while cnode:
                s+=repr(cnode.value)
                if cnode.next:
                    s+=', '
                cnode = cnode.next
            s +=']'
        return s


## testing
if __name__ == '__main__':
    ds = DoublyLinkedList()
    ds.push(1)
    ds.push(2)
    ds.push(3)
    print('traverse from head')
    cel = ds.head
    while cel:
        print ('c elem {}'.format(cel.value))
        cel = cel.next

    print('traverse from tail')
    cel = ds.tail
    while cel:
        print ('c elem {}'.format(cel.value))
        cel = cel.prev

    print(ds)
    print(ds.pop())
    print(ds)
    #pop elements until empty list
    x = ds.pop()
    y = ds.pop()
    print(ds)
