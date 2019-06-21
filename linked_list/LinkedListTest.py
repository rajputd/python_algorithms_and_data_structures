import unittest
from LinkedList import LinkedList, LinkedListNode

class TestBinarySearchRecursive(unittest.TestCase):

    def test_get(self):
        linkedlist = LinkedList(1)
        self.assertEqual(linkedlist.get(0), 1, "Should be 1")

    def test_append(self):
        linkedlist = LinkedList(5)
        linkedlist.append(4)
        linkedlist.append(3)
        linkedlist.append(2)
        self.assertEqual(linkedlist.get(3), 2, "Should be 2")
        self.assertEqual(linkedlist.get(2), 3, "Should be 3")
        self.assertEqual(linkedlist.get(1), 4, "Should be 4")


if __name__ == '__main__':
    unittest.main()