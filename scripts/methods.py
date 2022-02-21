from typing import List

import numpy as np
from scipy import ndimage

class Solution:
        def is_safe(
            self, grid: List[List[int]], row: int, col: int, visited
        ) -> bool:
            return (
                0 <= row < len(grid)
                and 0 <= col < len(grid[0])
                and grid[row][col] == 1
                and visited[row][col] == False
            )

        def dfs(
            self,
            row: int,
            col: int,
            visited: List[List[bool]],
            grid: List[List[int]],
        ) -> None:
            valid_row = [-1, 0, 0, 1, -1, 1, 1, -1]
            valid_col = [0, -1, 1, 0, -1, -1, 1, 1]
            visited[row][col] = True
            for neighbour in range(len(valid_row)):
                new_row = row + valid_row[neighbour]
                new_col = col + valid_col[neighbour]
                if self.is_safe(grid, new_row, new_col, visited):
                    self.dfs(new_row, new_col, visited, grid)

        def count_islands(self, grid: List[List[int]]) -> int:
            visited = [
                [False for col in range(len(grid[0]))]
                for row in range(len(grid))
            ]
            count = 0
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 1 and visited[row][col] == False:
                        self.dfs(row, col, visited, grid)
                        count += 1
            return count

def dfs(islands_arr):
    return Solution().count_islands(islands_arr)


def scipy_label(islands_arr):
    return ndimage.label(islands_arr, np.ones((3, 3)))[1]
