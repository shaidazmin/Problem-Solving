class Solution:
    def sumOfDigits (self, N):
        result = 0
        for c in str(N):
            result+=(int(c))
        return result


print(Solution().sumOfDigits(12))