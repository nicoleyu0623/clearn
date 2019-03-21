import unittest
import copy
from LinkedQueue import LinkedQueue

class LinkedQueueTest(unittest.TestCase):
    def setUp(self):
        self._queue_e0 = LinkedQueue()

        self._queue_e2 = LinkedQueue()
        self._queue_e2.enqueue("one")
        self._queue_e2.enqueue("two")


    def tearDown(self):
        pass

    def test_emptyStack(self):
        """check empty queuee"""
        q = copy.deepcopy(self._queue_e0)
        self.assertTrue(q.is_empty())

    def test_enqueue(self):
        q = copy.deepcopy(self._queue_e0)
        q.enqueue("one")
        self.assertEqual(q.first(), "one")
        q.enqueue("two")
        self.assertEqual(len(q),2)

    def test_dequeue(self):
        q = copy.deepcopy(self._queue_e2)
        res = q.dequeue()
        self.assertEqual(res, "one")
        self.assertEqual(len(q),1)


if __name__ == '__main__':
    unittest.main()
