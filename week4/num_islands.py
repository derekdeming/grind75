#  200 

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0

        # Function to perform DFS on the grid
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return

            # Mark the land as visited by setting it to '0'
            grid[i][j] = '0'

            # Visit all adjacent lands
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If land is found, perform DFS and increment island count
                if grid[i][j] == '1':
                    dfs(i, j)
                    num_islands += 1

        return num_islands
