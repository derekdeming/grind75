# 62 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # actually will use a 2D array here instead of 1D array like before 
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]