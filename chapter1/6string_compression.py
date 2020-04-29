import unittest
from collections import Counter

#note the text suggests to use a stringbuilder(in java) or some type of initial space
#allocation for the compressed string to avoid the 0(n^2) complexity of string concatenation.
#I'm not sure this is possible in regular python because you cannot allocate a string to a certain size
#or a list in the same way you can in other languages. you can allocate a list to all nones but 
#it still fills the list and does all of the appends under the hood. i'm not sure there is a more optimal
#way to do this than the below in python. 
def string_compression(uncompressed_string: str) -> str:
    current_char = uncompressed_string[0]
    current_count = 0
    compressed_string = ""
    for char in uncompressed_string:
        if char == current_char:
            current_count += 1
        else:
            compressed_string += f"{current_char}{current_count}"
            current_char = char
            current_count = 1
    compressed_string += f"{current_char}{current_count}"
 
    if len(compressed_string) < len(uncompressed_string):
        return compressed_string
    return uncompressed_string

class Test(unittest.TestCase):
    def test_string_compression(self):
        result = string_compression("aabcccccaaa")
        self.assertEquals(result, "a2b1c5a3")
        result = string_compression("abcccd")
        self.assertEquals(result, "abcccd")

if __name__ == "__main__":
    unittest.main()

