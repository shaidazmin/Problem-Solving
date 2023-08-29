
class Solution:
    def sumOfMatrix(self,N,M,Grid):
        res = 0
        for row in range(N):
            for col in range(M):
                res += Grid[row][col]
        return res
    
print(Solution().sumOfMatrix(2,3,[[1,0,1],[-8,9,-2]]))    