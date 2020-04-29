import unittest
from typing import List

# you are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. 
# write a method to merge B into A in sorted order. 

def sorted_merge(a, b) -> List[int]:
    # this is very similar to merge method in merge sort
    # except since array 1 is already in place, we should zip elements in from the back
    a_idx = len(a) - len(b) - 1
    b_idx = len(b) - 1
    # index to insert the next sorted element
    out_idx = len(a) -1
    while(b_idx >= 0):
        if(b[b_idx] >= a[a_idx]):
            # put b in place at the end
            a[out_idx] = b[b_idx]
            out_idx -= 1
            b_idx -= 1
        else:
            # value in a is greater
            a[out_idx] = a[a_idx]
            a_idx -= 1
            out_idx -= 1
    return a

class Test(unittest.TestCase):
    '''Test Cases'''
    def test_sorted_merge(self):
        a = [1, 5, 6, 0, 0, 0]
        b = [2, 4, 9]
        expected = [1, 2,4, 5, 6, 9]
        actual = sorted_merge(a, b)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()