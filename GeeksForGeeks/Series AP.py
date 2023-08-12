
class Solution:
    def nthTermOfAP(self,A1,A2,N):
        return A1 + (N-1) * (A2-A1)


print(Solution().nthTermOfAP(100,7,3))
# print(Solution().nthTermOfAP(2,3,4))

