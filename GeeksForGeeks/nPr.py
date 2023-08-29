class Solution:
    def nPr(self, n, r):
        def fact(num):
            if num == 0:
                return 1
            else:
                return num * fact(num - 1)
        return fact(n) // fact(n-r)    
    
print(Solution().nPr(2,1))    