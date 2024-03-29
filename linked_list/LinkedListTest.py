import unittest
from LinkedList import LinkedList, LinkedListNode

class TestLinkedList(unittest.TestCase):

    def test_get(self):
        linkedlist = LinkedList(1)
        self.assertEqual(linkedlist.get(0), 1, "Should be 1")

    def test_get_fails_on_invalid_index(self):
        linkedlist = LinkedList(2)
        passTest = False
        try:
            linkedlist.get(10)
        except IndexError:
            passTest = True

        self.assertEqual(True, passTest, "Did not throw index error when given invalid index.")


    def test_append(self):
        linkedlist = LinkedList(5)
        linkedlist.append(4)
        linkedlist.append(3)
        linkedlist.append(2)
        self.assertEqual(linkedlist.get(3), 2, "Should be 2")
        self.assertEqual(linkedlist.get(2), 3, "Should be 3")
        self.assertEqual(linkedlist.get(1), 4, "Should be 4")

    def test_len(self):
        linkedlist = LinkedList(5)
        self.assertEqual(len(linkedlist), 1, "Should be 1")

        linkedlist.append(4)
        linkedlist.append(3)
        self.assertEqual(len(linkedlist), 3, "Should be 3")

        linkedlist.append(-5)
        self.assertEqual(len(linkedlist), 4, "Should be 4")

    def test_insert_at_head(self):
        linkedlist = LinkedList(2)
        linkedlist.insert(0, 1)
        self.assertEqual(linkedlist.get(0), 1, "Should be 1")

    def test_insert_in_middle(self):
        linkedlist = LinkedList(1)
        linkedlist.append(3)
        linkedlist.insert(1, 2)
        self.assertEqual(linkedlist.get(1), 2, "Should be 2")

    def test_insert_at_end(self):
        linkedlist = LinkedList(1)
        linkedlist.append(2)
        linkedlist.insert(2, 3)
        self.assertEqual(linkedlist.get(2), 3, "Should be 3")

    def test_insert_at_invalid_index(self):
        linkedlist = LinkedList(1)
        passTest = False

        try:
            linkedlist.insert(10, 1)
        except IndexError:
            passTest = True

        self.assertEqual(True, passTest, "Did not throw IndexError when given out of bounds index")

    def test_del_at_head(self):
        linkedlist = LinkedList(1)
        linkedlist.delete(0)
        self.assertEqual(len(linkedlist), 0, "Size should be zero")

    def test_del_at_middle(self):
        linkedlist = LinkedList(1)
        linkedlist.append(2)
        linkedlist.append(3)
        linkedlist.delete(1)
        self.assertEqual(len(linkedlist), 2, "Size should be two")

    def test_del_at_end(self):
        linkedlist = LinkedList(1)
        linkedlist.append(2)
        linkedlist.append(3)
        linkedlist.delete(2)
        self.assertEqual(len(linkedlist), 2, "Size should be two")


if __name__ == '__main__':
    unittest.main()