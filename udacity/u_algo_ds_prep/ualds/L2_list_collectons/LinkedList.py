class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head

    def append(self,new_element):
        current = self.head
        if self.head:
            while current.next:          #seek end of list
                current = current.next
            current.next = new_element
        else:                            #list was empty
            self.head = new_element

    def printContents(self):
        if self.head is None:
            print("list is empty")
            return

        current = self.head
        while current:
             print(current.value)
             current = current.next  #traverse untill null


    def get_position(self,position):
        """get an element from a specified position
        assume the first position is 1
        return None if position is not in the list"
        return None if list is empty"""
        if self.head is None:
            return None

        current_index = 1
        current = self.head
        while current:
            if position == current_index:
                return current
            current = current.next
            current_index += 1
        return None                    #we traversed all but did not find position

    def insert(self,new_element, position):
        """Insert a new node at the given position.
        Assume the first position is 1
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        #empty list case
        if self.head is None:
            self.head = new_element
            new_element.next = None
            return

        #usual case
        current_index = 1
        current = self.head
        while current:
            if position - current_index == 1:
                new_element.next = current.next
                current.next = new_element
                return
            current = current.next
            current_index += 1
        #case position is bigger than list length
        last_element = self.get_position(current_index -1)
        last_element.next = new_element
        new_element.next = None


    def delete(self, value):
        """delete the first node with a given value"""
        #empty list case
        if self.head is None:
            return

        current = self.head
        #case when value = head.value
        if value == current.value:
                self.head  = current.next
                return
        #general case
        while current:
            if value == current.next.value:
                current.next = current.next.next
                return
            current = current.next


    def delete_answ(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def delete_me2(self,value):
        """delete the first occurency of the value"""

        current = self.head
        previous = None
        if self.head:
            while current.next:
                previous = current
                current = current.next
                if current.value == value:
                    previous.next = current.next
                    return
            if current.value == value:
                self.head = None

    def insert_m2(self,new_element, position):
        current = self.head
        pos = 1
        if self.head is None and position ==1:  #border case
            self.head = new_element
            return
        if self.head:       #general case
            if position == 1:
                self.head = new_element
                new_element.next = current
                return
            while current.next:
                pos += 1
                previous = current
                current = current.next
                if position == pos:
                    previous.next = new_element
                    new_element.next = current
                    return



def testingLinkedList():
    l1 = LinkedList()
    l1.printContents()

    l1.append(Element("one"))
    l1.append(Element("two"))
    l1.append(Element("three"))
    l1.append(Element("four"))
    l1.printContents()

    print("testing get_position")
    l0  = LinkedList()
    print("fetched from empty list: {0}".format(l0.get_position(1)))
    print("fetched from l1 list first : {0}".format(l1.get_position(1).value))
    print("fetched from l1 list 4th : {0}".format(l1.get_position(4).value))
    print("fetched from l1 list 5th : {0}".format(l1.get_position(5)))

    print("testing insert")
    l1.insert(Element("Myawo"),3)
    print("after insert for el 3")
    l1.printContents()
    print('after insert with bigger index')
    l1.insert(Element("Wohoo"),10)
    l1.printContents()

    print('after insertion into empty list')
    l0.insert(Element("Firster"),3)
    l0.printContents()

    print('testing deletion of myawo')
    l1.delete("Myawo")
    l1.delete("Wohoo")
    print('after deletion')
    l1.printContents()

def testingQuizLinkedList():
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    print("stest get head position")
    print(ll.get_position(1).value)
    print("Test get_position")
    # Should print 3
    print(ll.head.next.next.value)
    # Should also print 3
    print(ll.get_position(3).value)

    print("Test insert")
    ll.insert(e4,3)
    # Should print 4 now
    print(ll.get_position(3).value)


    print("test delete")
    ll.printContents()
    print("contents before deletion")

    ll.delete(1)
    # Should print 2 now
    print(ll.get_position(1).value)
    # Should print 4 now
    print(ll.get_position(2).value)
    # Should print 3 now
    print(ll.get_position(3).value)


def testDelete_m2():
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.delete_me2(1)
    print("after deleting a head el")
    ll.printContents()

    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    ll.delete_me2(2)
    print("after deleting a 2nd el")
    ll.printContents()

    ll = LinkedList()
    ll.append(Element(1))
    ll.append(Element(2))
    ll.append(Element(3))
    #ll.printContents()
    ll.delete_me2(3)
    print("after deleting a last 3rd el")
    ll.printContents()

def  makeListThreEls():
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    return ll


def testInsert_m2():

    ll = LinkedList()
    ll.insert(Element("one"),1)
    print("after inserting into empty list")
    ll.printContents()

    ll = makeListThreEls()
    #ll.printContents()
    ll.insert_m2(Element("one"),2)
    print("after inserting into non empty list in 2nd pos")
    ll.printContents()

    ll = makeListThreEls()
    ll.insert_m2(Element("four"),4)
    print("after inserting into non empty list in 4th pos. expect nothing")
    ll.printContents()



def main():
    #testingLinkedList()
    #testingQuizLinkedList()
    #testDelete_m2()
    testInsert_m2()

if __name__ == '__main__':
    main()
