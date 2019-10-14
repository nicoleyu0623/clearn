'''
Given the Stack class below, implement a Queue class using two stacks!
Note, this is a "classic" interview problem.
Use a Python list data structure as your Stack.
'''

#########################
# author solution

class Queue2Stacks(object):
    def __init__(self):
        self.instack=[]
        self.outstack=[]

    def enqueue(self,item):
        self.instack.append(item)

    def dequeue(self):
        #if not self.outstack:
        if len(self.outstack) == 0:
            #while self.instack:
            while len(self.instack) > 0:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


if __name__ == '__main__':
    q = Queue2Stacks()

    for i in range(5):
        q.enqueue(i)

    for i in range(5):
        print(q.dequeue())
