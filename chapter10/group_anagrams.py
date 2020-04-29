# write a method to sort an array of strings so that all the anagrams are next to eachoter
import unittest
from typing import List
from collections import defaultdict

def group_anagrams(strings: List[str]) -> List[str]:
    anagram_dict = defaultdict(list)
    for string in strings:
        # sort the string
        sorted_str = ''.join(sorted(string.lower()))
        # put the string into a dict
        anagram_dict[sorted_str].append(string)
    # convert the hashmap back into an array with all values of a key 
    # next to eachother
    out_arr = []
    for (key, values) in anagram_dict.items():
        for value in values:
            out_arr.append(value)
    return out_arr


class Test(unittest.TestCase):
    '''Test Cases'''
    def test_sorted_merge(self):
        strings = [0] * 8
        strings[0] = "abed"
        strings[1] = "later"
        strings[2] = "bead"
        strings[3] = "alert"
        strings[4] = "altered"
        strings[5] = "bade"
        strings[6] = "alter"
        strings[7] = "alerted"
        result = group_anagrams(strings)
        print(result)    

if __name__ == "__main__":
    unittest.main()