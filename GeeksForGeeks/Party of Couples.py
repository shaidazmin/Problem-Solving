class Solution:
    def findSingle(self, N, arr):
        # code here
        res = 0
        for i in arr:
            res = res ^ i
        return res     
    

# print(Solution().findSingle(5,[1, 2, 3, 2, 1]))   
# print(Solution().findSingle(11,[1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6]))   


