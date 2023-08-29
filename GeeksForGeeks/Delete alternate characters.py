#User function Template for python3
class Solution:
    def delAlternate (ob, S):
        S = str(S)
        res = ''
        for i in range(len(S)):
            if i %2 == 0:
                res+=S[i]
        return res


print(Solution().delAlternate("Geeks"))