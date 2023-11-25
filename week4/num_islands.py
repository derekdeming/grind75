#  200 

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: #grid = empty 
            return 0

        num_islands = 0

        # depth first search on grid -- 
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return

            # setting it to 0 if seen
            grid[i][j] = '0'

            # should traverse the adjacent parts 
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if found use DFS and increment island count
                if grid[i][j] == '1':
                    dfs(i, j)
                    num_islands += 1

        return num_islands

'''
use dfs on unvisited cell. it should traverse and mark connected cells 
'''