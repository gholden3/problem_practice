# Given a collection of intervals, merge all overlapping intervals.
import unittest
from typing import List, Tuple

def mykey(tuple):
    return tuple[0]

def sort_ranges(arr: List[Tuple[int, int]]) -> None:
    arr.sort( key=mykey)

def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if len(intervals) <= 1:
            return intervals
    # sort every range by the starting value
    sort_ranges(intervals)
    # go through every pair and if the starting range falls within the range
    # before it, merge it in
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

class Test(unittest.TestCase):
    '''Test Cases'''
    def test_merge_intervals(self):
        input = [[1, 3], [5, 9], [15,18], [8,10], [2,6]]
        expected_output = [[1,10],[15,18]]
        actual = merge_intervals(input)
        self.assertEqual(expected_output, actual)

if __name__ == "__main__":
    unittest.main()