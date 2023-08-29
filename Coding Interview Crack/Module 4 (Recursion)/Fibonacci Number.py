# Problem URL
# https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1)+ self.fib(n-2)
    
    def fib_using_memo(self, n):
        seen = {}
        def memo_recursion(n, seen):
            if n == 0 or n ==1:
                return n
            if n not in seen:
                seen[n] = memo_recursion(n-1, seen) + memo_recursion(n-2, seen)
            return seen[n] 
        
        return memo_recursion(n, seen)
    
    def memorization(self,n):
        dp = {}
        dp[0] = 0
        dp[1] = 1 
        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]    
        return dp[n]    
     


print(Solution().fib(2))        
print(Solution().memorization(2))     
  
