# Problem URL
# https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        return pow(x,n)

print(Solution().myPow(2,10))        