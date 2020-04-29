import unittest
from typing import List
from math import floor

def merge_sort(input_arr: List[int]) -> List[int]:
    helper = [0]* len(input_arr)
    return mergesort(input_arr, helper, 0, len(input_arr) -1)

def mergesort(array: List[int], helper: List[int], low: int,  high: int):
    if low < high:
        middle = floor((low + high) / 2)
        # sort the left half
        array = mergesort(array, helper, low, middle) 
        # sort the right half
        array = mergesort(array, helper, middle +1, high)
        # merge the left and the right
        array = merge(array, helper, low, middle, high)
    # stop condition: low==high. you are just calling on one element. 
    # in this case you just do nothing and return.
    return array

def merge(array: List[int], helper: List[int], low: int, middle: int, high: int) -> List[int]:
    # copy both halves into one helper array
    for (index, _val) in enumerate(array):
        helper[index] = array[index] 
    # since we know the two halves are already sorted (left and right), we just have to go one
    # by one and write them into the output array. 

    # initialize three indeces, one for reading left, one for reading right, and one for writing into output arr
    left_index = low
    right_index = middle + 1
    out_arr_index = low

    while (left_index <= middle and right_index <= high):
        if helper[left_index] <= helper[right_index]:
            # the smaller element is on the left half
            array[out_arr_index] = helper[left_index]
            left_index += 1
        else:
            # right element is smaller
            array[out_arr_index] = helper[right_index]
            right_index += 1
        out_arr_index += 1

    # once we are finished going through one half of the helper, if there are any remaining elements in the left half of the helper, 
    # we copy them over to output array. if there are remaining items in right half, we don't 
    # have to do anything because they are already in place
    for i in range(left_index, middle+1):
        array[out_arr_index] = helper[i]
        out_arr_index += 1
    return array        

class TestMerge(unittest.TestCase):
    test_arr = [9, 7, 3, 2, 5]
    def test_merge_sort(self):
        expected_arr = [2, 3, 5, 7, 9]
        response = merge_sort(self.test_arr)
        self.assertEqual(expected_arr, response)

        test_arr_2 = [9, 7, 2, 5]
        expected_arr = [2, 5, 7, 9]
        response = merge_sort(test_arr_2)
        self.assertEqual(expected_arr, response)

if __name__ == "__main__":
    unittest.main()