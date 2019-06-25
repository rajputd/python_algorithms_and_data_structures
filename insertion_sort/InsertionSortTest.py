import unittest
from InsertionSort import insertionSort

class TestinsertionSort(unittest.TestCase):

    def test_already_sorted(self):
        input = [0,1,2,3,4,5]
        self.assertEqual(insertionSort(input), sorted(input), "Should be [0,1,2,3,4,5]")

    def test_empty_array(self):
        input = []
        self.assertEqual(insertionSort(input), sorted(input), "Should be []")

    def test_unsorted_array(self):
        input = [1, 5, 63, 3, 54, 1]
        self.assertEqual(insertionSort(input), sorted(input), "Should be [1, 1, 3, 5, 54, 63]")

    def test_backwards_array(self):
        input = [5, 4, 3, 2, 1]
        self.assertEqual(insertionSort(input), sorted(input), "Should be [1, 2, 3, 4, 5]")


if __name__ == '__main__':
    unittest.main()