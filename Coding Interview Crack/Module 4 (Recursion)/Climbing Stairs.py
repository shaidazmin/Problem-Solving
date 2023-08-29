# Problem URL
# https://leetcode.com/problems/climbing-stairs/description/
# Not properly understand


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
    
        # Initialize an array to store the number of ways for each step
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        # Fill in the array using dynamic programming
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    

print(Solution().climbStairs(10))    