import time
from typing import List

import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

import methods


def dfs_method(islands_arr: List[List[int]]) -> float:
    islands_arr = islands_arr.tolist()
    time_start = time.time()
    methods.dfs(islands_arr)
    time_end = time.time()
    return time_end - time_start


def scipy_label_method(islands_arr: List[List[int]]) -> float:
    time_start = time.time()
    methods.scipy_label(islands_arr)
    time_end = time.time()
    return time_end - time_start


def main():
    # Make tests repetable.
    np.random.seed(0)

    size_list = [5, 10, 20, 50, 100, 200, 500, 1000]
    dfs_method_times = []
    label_method_times = []

    for size in size_list:
        # Create a random sqare array with 0's and 1's.
        islands_arr = np.random.choice([0, 1], size=(size, size), p=[0.7, 0.3])

        # Append execution times to corresponding lists.
        dfs_method_times.append(dfs_method(islands_arr))
        label_method_times.append(scipy_label_method(islands_arr))

    # Plot execution time against array size.
    plt.figure()
    plt.plot(size_list, dfs_method_times, label="DFS")
    plt.plot(size_list, label_method_times, label="Scipy")
    plt.xscale("log")
    plt.xlabel("Side length of square array")
    plt.ylabel("Execution time [s]")
    plt.title(
        "Comparison of running times of DFS-based algorithm and Scipy's ndimage method"
    )
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
