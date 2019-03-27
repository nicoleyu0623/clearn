#--------------------------------------------#
class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        print('  trace call: SimpleList.add()')
        self._items.append(item)

    def __getitem__(self, index):  #protocol of collection
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):            #protocol of collection
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)

#------------------------------------------------#
class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()             #els are sorted  at instantatiation

    def add(self, item):     #list is resorted
        print('  trace call: SortedList.add()')
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))
#------------------------------------------------#
class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)  #validating items
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        print('  trace call: IntList.add()')
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return "IntList({!r})".format(list(self))

#------------------------------------------------#
class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return 'SortedIntList({!r})'.format(list(self))
#------------------------------------------------#

