# 322

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # A large number for initialization, larger than any possible number of coins
        MAX = amount + 1

        # Initialize an array (dp) with each element representing 
        # the minimum number of coins needed for that amount
        # All elements are initially set to MAX, except dp[0] which is set to 0
        dp = [MAX] * (amount + 1)
        dp[0] = 0

        # Iterate over each amount from 1 to the total amount
        for a in range(1, amount + 1):
            # For each coin, check if it can contribute to the current amount
            for coin in coins:
                if coin <= a:
                    # Update the dp array for this amount as the minimum of its current value
                    # and the number of coins needed for the remaining amount after using this coin
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        # If dp[amount] is still MAX, it means the amount cannot be made up by any combination of the coins
        return dp[amount] if dp[amount] != MAX else -1
