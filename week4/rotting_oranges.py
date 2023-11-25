#  994 

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) # get dimensions of grid
        fresh_count = 0
        queue = deque()

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:  # if the orange is rotten thenb add 
                    queue.append((r, c))
                elif grid[r][c] == 1: # if the orange is freshthen increment
                    fresh_count += 1

        minutes_passed = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # r, down, l, up respectively 

        # BFS process
        while queue and fresh_count > 0:
            minutes_passed += 1
            for _ in range(len(queue)): #processing all oranges at the current timestep 
                x, y = queue.popleft()
                for dx, dy in directions: #check neighbors within boundaries 
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_count -= 1

        return minutes_passed if fresh_count == 0 else -1

'''
find the min amount of time it take for all oranges to become rotten

use BFS to find the shortest path to all oranges

'''