import unittest
from typing import List
from math import floor

def partition(arr: List[int], left_idx: int, right_idx: int) -> int:
    # index of the last small element in sorted array
    i = left_idx -1
    # choose pivot point
    pivot: int = arr[right_idx]
    for current_idx in range(left_idx, right_idx):
        # if current element is smaller than or equal to pivot
        if arr[current_idx] <= pivot:
            # increment index of smaller element
            i += 1
            # put current element into the next slot for small elements and 
            # take the value that was there ant put it into current index
            arr[i], arr[current_idx] = arr[current_idx], arr[i]
    # finally place the pivot in the right place by swapping it with the first 
    # large value
    arr[i+1], arr[right_idx] = arr[right_idx], arr[i + 1]
    # return the index where the pivot point is
    return (i + 1)


def quick_sort(input_arr: List[int], left_idx: int, right_idx: int):
    ''' given an array and left and right index to start working on, sort the array'''
    if(left_idx < right_idx):
        pi = partition(input_arr, left_idx, right_idx)
        # input_arr[pi] is now at the right place
        # now we sort elements before partition and after partition
        quick_sort(input_arr, left_idx,  pi - 1)
        quick_sort(input_arr, pi + 1, right_idx)

def run_quick_sort(input_arr: List[int]) -> List[int]:
    return quick_sort(input_arr, 0, len(input_arr) - 1)


class TestQuicksort(unittest.TestCase):
    test_arr = [9, 7, 3, 2, 5]
    def test_quick_sort(self):
        expected_arr = [2, 3, 5, 7, 9]
        run_quick_sort(self.test_arr)
        self.assertEqual(expected_arr, self.test_arr)

        test_arr_2 = [9, 7, 2, 5]
        expected_arr = [2, 5, 7, 9]
        run_quick_sort(test_arr_2)
        self.assertEqual(expected_arr, test_arr_2)

if __name__ == "__main__":
    unittest.main()