# 70 

class Solution: 
    def climbStairs(self, n: int) -> int: 
        if n <= 1: 
            return n 
        steps = [0] * (n + 1) 
        steps[0], steps[1] = 1, 1
        for i in range(2, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]
    
'''
there is only 1 way to climb 0 and 1 so return 1

    - create an array of size n + 1 to store the number of ways to climb to each step
    - steps[i] represents the number of ways to climb to step i
    steps[i - 1] and steps[i - 2] represent both ways to climb 
'''