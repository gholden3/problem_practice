import unittest
from typing import List
from math import floor

def run_binary_search(arr: List[int], value: int) -> int:
    ''' given a sorted array, find the index where a value occurs'''
    return binary_search(arr, value, 0, len(arr))

def binary_search(arr: List[int], value, low: int, high: int):
    if low > high:
        return -1
    mid = floor((low + high)/2)
    if (arr[mid] < value):
        # search right
        return binary_search(arr, value, mid+1, high )
    elif (arr[mid] > value):
        # search left
        return binary_search(arr, value, low, mid - 1)
    return mid

class Test(unittest.TestCase):
    '''Test Cases'''
    def test_binary_search(self):
        arr = [1, 3, 3, 5, 6, 7, 8]
        idx = run_binary_search(arr, 5)
        self.assertEqual(3, idx)

if __name__ == "__main__":
    unittest.main()