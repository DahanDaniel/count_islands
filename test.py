import unittest

import numpy as np

import methods
import main


class TestEditChecks(unittest.TestCase):
    def test_results(self):
        # Test correctness of returned values for example input.
        arrays_and_result_dict = {
            0: np.zeros((4, 5)),
            5: np.array(
                [
                    [1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 1],
                    [1, 0, 0, 1, 1],
                    [0, 0, 0, 0, 0],
                    [1, 0, 1, 0, 1],
                ]
            ),
            1: np.ones((2, 1)),
        }

        for n_islands, islands_arr in arrays_and_result_dict.items():
            self.assertEqual(n_islands, methods.scipy_label(islands_arr))

    def test_raised_errors(self):
        # Provided array has invalid shape.
        file_path_shape = r"test_arrays/invalid_shape.txt"
        self.assertRaises(ValueError, main.main, file_path_shape)

        # Provided array has invalid characters.
        file_path_characters = r"test_arrays/invalid_characters.txt"
        self.assertRaises(ValueError, main.main, file_path_characters)

        # Provided file path is invalid.
        file_path_invalid = r"test_arrays/this_file_does_not_exist.txt"
        self.assertRaises(IOError, main.main, file_path_invalid)

        # Invalid file extention.
        file_path_extention = r"test_arrays/invalid_extention.py"
        self.assertRaises(IOError, main.main, file_path_extention)


if __name__ == "__main__":
    unittest.main(exit=False)
