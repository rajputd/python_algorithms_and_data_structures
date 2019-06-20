import unittest
from binary_search_recursive import binary_search_recursive

class TestBinarySearchRecursive(unittest.TestCase):

    def test_search_for_lowest_val(self):
        arr = [1,2,3,4,5]
        val = 1
        result = binary_search_recursive(arr, val, 0, len(arr) - 1)
        self.assertEqual(result, 0, "Should be 0")

    def test_search_for_highest_val(self):
        arr = [1,2,3,4,5]
        val = 5
        result = binary_search_recursive(arr, val, 0, len(arr) - 1)
        self.assertEqual(result, 4, "Should be 4")

    def test_search_for_immediately_finding_val(self):
        arr = [1,2,3,4,5]
        val = 3
        result = binary_search_recursive(arr, val, 0, len(arr) - 1)
        self.assertEqual(result, 2, "Should be 2")

    def test_search_for_unfindable_high_val(self):
        arr = [1,2,3,4,5]
        val = 1000
        result = binary_search_recursive(arr, val, 0, len(arr) - 1)
        self.assertEqual(result, -1, "Should be -1")

    def test_search_for_unfindable_low_val(self):
        arr = [1,2,3,4,5]
        val = -100
        result = binary_search_recursive(arr, val, 0, len(arr) - 1)
        self.assertEqual(result, -1, "Should be -1")

if __name__ == '__main__':
    unittest.main()