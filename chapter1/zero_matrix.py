# write functionthat accepts an MxN matrix and returns a matrix that has filled the corresponding 
# row and column equal to zero for every zero found in the matrix

import unittest
from typing import List

def make_row_zeros(row_index: int, matrix: List[List[int]]) -> List[List[int]]:
    ''' given an index and a matrix, replace every element in that row with zeros'''
    row_length = len(matrix[0])
    for col_idx in range(0, row_length):
        matrix[row_index][col_idx] = 0
    return matrix

def make_cols_zeros(col_index: int, matrix: List[List[int]]) -> List[List[int]]:
    ''' given an index and a matrix, replace every element in that column with zeros'''
    col_length = len(matrix)
    for row_idx in range(0, col_length):
        matrix[row_idx][col_index] = 0
    return matrix

def zero_matrix(input_matrix: List[List[int]]) -> List[List[int]]:
    rows_containing_zeros = []
    cols_containing_zeros = []

    for row_idx, row in enumerate(input_matrix):
        for col_idx, val in enumerate(row):
            if val == 0:
                rows_containing_zeros.append(row_idx)
                cols_containing_zeros.append(col_idx)

    for row_containing_zero in rows_containing_zeros:
        input_matrix = make_row_zeros(row_containing_zero, input_matrix)
    for col_containing_zero in cols_containing_zeros:
        input_matrix = make_cols_zeros(col_containing_zero, input_matrix)
    return input_matrix


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1,    2,    3,  4,   0],
            [6,    0,    8,  9,   10],
            [11,   12,   13, 14,  15],
            [16,   0,    18, 19,  20],
            [21,   22,   23, 24,  25]
        ], [
            [0,    0,   0,    0,  0],
            [0,    0,   0,    0,  0],
            [11,   0,   13,   14, 0],
            [0,    0,   0,    0,  0],
            [21,   0,   23,   24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()