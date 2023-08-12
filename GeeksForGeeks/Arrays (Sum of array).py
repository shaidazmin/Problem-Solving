class Solution:
    def getSum(self, arr, n):
        sum = 0
        for i in arr:
            sum+=i
        return sum    


print(Solution().getSum([1,2,3,4], 4))