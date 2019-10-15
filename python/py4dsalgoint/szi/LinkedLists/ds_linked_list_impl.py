'''

singly linked list is a sequence of linked nodes

LinkedList contains a reference to head element
Linked List can have a push() and pop()  and get(element) methods
'''


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):


    def __init__(self):
        self.head = None
        self.length = 0

    def push(self,item):
        node = Node(item)
        if self.head:   #head is not empty
            node.next = self.head
        self.head = node
        self.length +=1

    def pop(self):
        if self.length > 0:
            item = self.head.value
            self.head = self.head.next
            self.length -= 1
            return item
        else:
            return None

    def get(self,item):

        cnode = self.head
        while cnode:
            if cnode.value == item:
                break
            cnode = cnode.next

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

### testing
if __name__ == '__main__':
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    print(ll)
    print(ll.pop())
    print(ll)
