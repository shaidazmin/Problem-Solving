#User function Template for python3

class Solution:
    def mean(self, N , A):
        # code here 
        res = 0
        for i in A:
            res += i
        return res // N


print(Solution().mean(4, [ 78 , 89 , 67 , 76]))
