'''
Specs:
Stack() creates a new empty stack
push(item) puts item on the top
pop() #removes item from the top
peek() return item from the top without removing it
isEmpty()
size() return number of elements
'''


class Stack(object):
    def __init__(self):
        self.items= []  #will use python list as a storage of elements

    def isEmpty(self):
        return self.items == []


    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]   #retuns last element in the list

    def size(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)

from pprint import pprint as pp
if __name__ == '__main__':
    s = Stack()
    pp(s.isEmpty())
    s.push(1)
    s.push('two')
    pp(s.peek())
    s.push(True)
    pp(s)
    pp(s.size())
    x = s.pop()
    pp(s)
