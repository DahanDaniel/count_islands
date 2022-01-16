import os
import sys

import numpy as np
from scipy import ndimage

import methods


def main(file_path):
    # Check if provided file path is valid.
    if not os.path.isfile(file_path):
        raise FileNotFoundError("Error: Invalid file path.")
    elif not file_path.endswith(".txt"):
        raise IOError("Error: Invalid file extention.")

    # Read data from file and check if the shape is valid.
    try:
        islands_arr = np.loadtxt(file_path)
    except ValueError as e:
        raise e

    # Check for errors, array shape, invalid characters...
    if not np.isin(islands_arr, [0, 1]).all():
        raise ValueError("Error: Input array has invalid characters.")

    # Count islands.
    n_islands = methods.scipy_label(islands_arr)

    # Print output.
    print(n_islands)


if __name__ == "__main__":
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        raise FileNotFoundError("Error message")
    main(file_path)
