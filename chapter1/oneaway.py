# there are 3 types of edits that can be performed on strings: insert, remove, replace. given 2 strings, 
# write a function to check if they are one or zero edits away
import unittest

def check_for_removal(test_string, original_string):
    indices_to_check = range(0, len(original_string) - 2)
    for index in indices_to_check:
        if(original_string[index] != test_string[index]):
            return (original_string[index+1:-1] == test_string[index:-1])
        return True

def check_for_insertion(test_string, original_string):
    for index, char in enumerate(original_string):
        if(char != test_string[index]):
            return (original_string[index:-1] == test_string[index+1:-1])

def check_for_replacement(test_string, original_string):
    for index, char in enumerate(original_string):
        if(char != test_string[index]):
            return (original_string[index+1:-1] == test_string[index+1:-1])
                

def one_away(test_strings):
    (original_string, test_string) = test_strings
    if(original_string == test_string):
        return True
    insert_length = len(original_string) + 1
    remove_length = len(original_string) - 1
    test_string_length = len(test_string)
    original_string_length = len(original_string)

    if(test_string_length == original_string_length):
        return check_for_replacement(test_string, original_string)
    if(original_string_length - 1 == test_string_length):
        return check_for_removal(test_string, original_string)
    if(original_string_length + 1 == test_string_length):
        return check_for_insertion(test_string, original_string)
    # lengths are not within one char of eachother
    return False


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        (['pale', 'ple'], True),
        (['pales', 'pale'], True),
        (['pale', 'bale'], True),
        (['pale', 'palie'], True),
        (['pale', 'bake'], False)]

    def test_one_away(self):
        for [test_strings, expected] in self.data:
            print("testing " + test_strings[0] + " " + test_strings[1])
            actual = one_away(test_strings)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()