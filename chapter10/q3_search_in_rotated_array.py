# Given a sorted array of n integers which has been rotated an unknown
# number of times, write code to find an element in that array. you may assume
# the array was originally sorted in ascending order
import unittest
from math import floor

def run_search_in_rotated_array(array, value_to_find: int) -> int:
    ''' searches a rotated array. returns the index where the value was found'''
    return search_in_rotated_array(array, value_to_find, 0, len(array) - 1)

def search_in_rotated_array(array, value_to_find, low_idx, high_idx):
    mid_idx = floor((high_idx + low_idx)/2)
    mid_val = array[mid_idx]
    if (value_to_find == mid_val):
        return mid_idx
    left_normally_ordered: bool = (array[low_idx] < array[mid_idx])
    right_normally_ordered: bool = (array[high_idx] > array[mid_idx])
    left_all_repeats: bool = (array[mid_idx] ==  array[low_idx])
    right_all_repeats: bool = (array[mid_idx] ==  array[high_idx])
    if left_normally_ordered:
        if value_to_find in range(low_idx, mid_idx):
            # value is in the left
            return search_in_rotated_array(array, value_to_find, low_idx, mid_idx - 1)
        else:
            # value is in the right
            return search_in_rotated_array(array, value_to_find, mid_idx + 1, high_idx)
    elif right_normally_ordered:
        if value_to_find in range(mid_idx + 1, high_idx):
            # value is in the right
            return search_in_rotated_array(array, value_to_find, mid_idx + 1, high_idx)
        else:
            # value is in the left
            return search_in_rotated_array(array, value_to_find, low_idx, mid_idx - 1)
    elif left_all_repeats:
        # we know the repeats does not contain our value so search right
        return search_in_rotated_array(array, value_to_find, mid_idx +1, high_idx)
    elif right_all_repeats:
        return search_in_rotated_array(array, value_to_find, low_idx, mid_idx -1 )
    

class Test(unittest.TestCase):
    def test_search_in_rotated_array(self):
        test_cases = [
            ([15, 16, 19, 20, 1, 3, 5, 7, 10], 5, 6),
            ([2, 2, 2, 3, 4, 2], 2, 2),
            ([2, 2, 2, 3, 4, 2], 4, 4)
        ]
        for test_case in test_cases:
            (array, search_val, expected_idx) = test_case
            index = run_search_in_rotated_array(array, search_val)
            self.assertEqual(expected_idx, index)


if __name__ == "__main__":
    unittest.main()
