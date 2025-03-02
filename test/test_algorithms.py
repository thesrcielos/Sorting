import unittest
from sorting import algorithms

arrays = [[10, 2, 5, 613, 65, 345, 73, 23, 67, 0], [], [2], [12, 56, 3, 54, 57, 2, 32], [6, 5, 4, 3, 2, 1]]
expected = [[0, 2, 5, 10, 23, 65, 67, 73, 345, 613], [], [2], [2, 3, 12, 32, 54, 56, 57], [1, 2, 3, 4, 5, 6]]


class AlgorithmsTests(unittest.TestCase):
    def test_heap_sort(self):
        for i in range(len(arrays)):
            array = arrays[i].copy()
            result = algorithms.heap_sort(array)
            self.assertEqual(result, expected[i])

    def test_quick_sort(self):
        for i in range(len(arrays)):
            array = arrays[i].copy()
            result = algorithms.quick_sort(array)
            self.assertEqual(result, expected[i])

    def test_selection_sort(self):
        for i in range(len(arrays)):
            array = arrays[i].copy()
            result = algorithms.selection_sort(array)
            self.assertEqual(result, expected[i])


if __name__ == "__main__":
    unittest.main()
