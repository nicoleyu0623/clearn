
#-------- quiz queue practice -------
class Queue:

    def __init__(self, head=None):
        if head:
            self.storage = [head]
        else:
            self.storage = []

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def printElements(self):
        print(self.storage)

    def peek(self):
        if (len(self.storage) == 0 ):
            return None
        return self.storage[0]

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        answer = self.storage[0]
        self.storage.remove(answer)
        return(answer)


def testQuizQueuePractice():
    # Setup
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test peek
    # Should be 1
    print(q.peek())  # [1,2,3]

    # Test dequeue
    # Should be 1
    print(q.dequeue())  # [2,3]

    # Test enqueue
    q.enqueue(4)  # [2,3,4]
    # Should be 2
    print(q.dequeue())  # [3,4] returns 3
    # Should be 3
    print(q.dequeue())  # [4]  returns 3
    # Should be 4
    print(q.dequeue())  # [] returns 4
    q.enqueue(5)  # [5]
    # Should be 5
    print(q.peek())  # [5] returns 5

def main():
    testQuizQueuePractice() # pass OK

if __name__ == '__main__':
        main()