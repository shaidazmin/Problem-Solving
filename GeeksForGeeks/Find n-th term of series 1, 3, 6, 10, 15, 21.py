class Solution:
    def findNthTerm(self, N):
        return N * (N+1) // 2 


print(Solution().findNthTerm(4))