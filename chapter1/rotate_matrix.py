# given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees
import unittest
from typing import List
from math import floor

def rotate_layer(matrix: List[List[int]], layer: int) -> List[List[int]]:
    '''given a layer index, rotate that layer of the matrix right by 90 degrees and return the matrix'''
    # account for rows around me
    layer_starting_index = layer
    layer_ending_index = (len(matrix) -1) - layer
    
    for i in range(layer_starting_index, layer_ending_index):
        offset = i - layer_starting_index
        top = matrix[layer_starting_index][i]
        # move left to top
        matrix[layer_starting_index][i] = matrix[layer_ending_index - offset][layer_starting_index]
        # move bottom to left
        matrix[layer_ending_index - offset][layer_starting_index] = matrix[layer_ending_index][layer_ending_index- offset]
        # move right to bottom
        matrix[layer_ending_index][layer_ending_index- offset] = matrix[i][layer_ending_index]
        # move top to right
        matrix[i][layer_ending_index] = top
    return matrix

def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    layers = range(0, floor(len(matrix)))
    for layer in layers:
        matrix = rotate_layer(matrix, layer)
    return matrix

class TestRotate(unittest.TestCase):
    startarr = [[1,   2,    3,    4  ],
                [5,   6,    7,    8  ],
                [9,   10,   11,   12 ],
                [13,  14,   15,   16 ]]

    expectedarr = [[13,   9,   5,   1],
                   [14, 10, 6, 2],
                   [15, 11, 7, 3],
                   [16, 12, 8, 4]]

    def test_rotate(self):
        output_arr = rotate_matrix(self.startarr)
        self.assertEqual(self.expectedarr, output_arr)

if __name__ == "__main__":
    unittest.main()