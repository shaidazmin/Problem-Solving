class Solution:
    def getTable(self,N):
        res = []
        for i in range(1,11):
            res.append(i*N)
        return res  
          

print(Solution().getTable(2))