class Solution:
    def IsPerfect(self,arr,n):
        return arr == arr[::-1]


print(Solution().IsPerfect([20, 4, 15, 10, 14, 19, 11, 8, 5, 19, 13, 8 ,18 ,13 ,3, 12 ,8 ,16 ,19 ,11], 5))