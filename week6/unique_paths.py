# 62 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # actually will use a 2D array here instead of 1D array like before 
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
    
'''
alternatively: we can use combinatorics **

initialize dp 2D table: dims m x n and each cell is = 1

there is only one way to reach any cell in the first row or first column (either keep moving right or keep moving down, respectively)

it then fills the rest of the dp table

The value of dp[i][j] (the number of unique paths to reach cell (i, j)) is the sum of the number of unique paths to reach the cell directly above it (dp[i - 1][j]) and the cell directly to its left (dp[i][j - 1]). 

This is because any path to (i, j) must come from either above or left.

dp[-1][-1] (or dp[m - 1][n - 1]) === total num of unique paths from the top-left corner to the bottom-right corner 
'''