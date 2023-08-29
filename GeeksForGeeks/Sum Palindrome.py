class Solution:
    def isSumPalindrome (self, n):
        res = str(n + int(str(n)[::-1]))
        return res if res == res[::-1] else 0
    
print(Solution().isSumPalindrome(23))    