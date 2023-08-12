class Solution:
    def evenlyDivides (self, N):
        # code here
        n = str(N)
        res = 0
        for i in n:
            if int(i) == 0:
                continue
            elif N % int(i) == 0:
                res+=1
        return res
    

print(Solution().evenlyDivides(2446))        