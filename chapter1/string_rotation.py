import unittest

# assume you have a method isSubstring which checks if one word is a substring of another.
# given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to 
# issubstring

def is_substring(s1: str, s2: str) -> bool:
    '''returns whether s2 is a substring of s1'''
    return True if s2 in s1 else False

def string_rotation(s1: str, s2: str) -> bool:
    ''' given s1 and s2, returns whether s2 is a rotation of s1'''
    s1_len = len(s1)
    s2_len = len(s2)
    if ((s1_len != s2_len) or (s1_len <= 0) or (s2_len <= 0)):
        return False
    return is_substring(s1 + s1, s2)

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()