class Solution:
    def mulClock(self, num1, num2):
        res = num1 * num2
        if res > 12:
            return str(res - 2)[-1:]
        return res
    
print(Solution().mulClock(2,4))    
print(Solution().mulClock(3,5))    