import unittest
from QuickSort import quickSort, partition

class TestquickSort(unittest.TestCase):

    def test_already_sorted(self):
        input = [0,1,2,3,4,5]
        output = input[:]
        quickSort(output, 0, len(output) - 1)
        self.assertEqual(output, sorted(input), "Should be [0,1,2,3,4,5]")

    def test_empty_array(self):
        input = []
        output = input[:]
        quickSort(output, 0, len(output) - 1)
        self.assertEqual(output, sorted(input), "Should be []")

    def test_unsorted_array(self):
        input = [1, 5, 63, 3, 54, 1]
        output = input[:]
        quickSort(output, 0, len(output) - 1)
        self.assertEqual(output, sorted(input), "Should be [1, 1, 3, 5, 54, 63]")

    def test_backwards_array(self):
        input = [5, 4, 3, 2, 1]
        output = input[:]
        quickSort(output, 0, len(output) - 1)
        self.assertEqual(output, sorted(input), "Should be [1, 2, 3, 4, 5]")

    def test_partition_on_already_sorted(self):
        input = [0,1,2,3,4,5]
        output = input[:]
        pivot = partition(output, 0, len(output) - 1)
        self.assertEqual(pivot, 5, "Pivot should be 5")
        for i in range(pivot):
            self.assertLess(output[i], output[pivot], str(output[i]) + " should be less than " + str(output[pivot]))

    def test_partition_on_unsorted(self):
        input = [1, 5, 63, 3, 54, 1]
        output = input[:]
        pivot = partition(output, 0, len(output) - 1)
        print(output)
        self.assertEqual(pivot, 0, "Pivot should be 0")
        for i in range(pivot):
            self.assertLess(output[i], output[pivot], str(output[i]) + " should be less than " + str(output[pivot]))

    def test_partition_on_backwards(self):
        input = [5, 4, 3, 2, 1]
        output = input[:]
        pivot = partition(output, 0, len(output) - 1)
        self.assertEqual(pivot, 0, "Pivot should be 0")
        for i in range(pivot):
            self.assertLess(output[i], output[pivot], str(output[i]) + " should be less than " + str(output[pivot]))

if __name__ == '__main__':
    unittest.main()