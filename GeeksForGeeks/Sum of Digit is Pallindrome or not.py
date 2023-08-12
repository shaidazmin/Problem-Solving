class Solution:
    def isDigitSumPalindrome(self,N):
        #code here
        if len(str(N)):
            s = str(N)
            sum = 0
            for i in s:
                sum += int(i)
            return  1 if str(sum) == str(sum)[::-1] else 0
        return 0


print(Solution().isDigitSumPalindrome(56))