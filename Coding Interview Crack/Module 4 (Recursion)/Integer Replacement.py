# Problem URL
# https://leetcode.com/problems/integer-replacement/
# Not properly understand

# Study on Recursion with Memoization 

class Solution(object):
    
    def integerReplacement(self, n):
        
        memo = {}
        if n in memo:
            return memo[n]
        
        if n == 1:
            return 0
        
        if n % 2 == 0:
            memo[n] = self.integerReplacement(n // 2) + 1
        else:
            memo[n] = min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1
        
        return memo[n]

# Test cases
print(Solution().integerReplacement(8))  # Output: 3
print(Solution().integerReplacement(7))  # Output: 4
print(Solution().integerReplacement(4))  # Output: 2