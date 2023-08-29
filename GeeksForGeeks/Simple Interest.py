class Solution:
    def simpleInterest(self,A,B,C):
        return format( ((A * B) / 100) * C,'.2f')
    
print(Solution().simpleInterest(100,20,2))    