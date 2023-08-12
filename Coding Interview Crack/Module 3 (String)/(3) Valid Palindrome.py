# Problem URL
# https://leetcode.com/problems/valid-palindrome/description/


class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(l.lower() for l in s if l.isalnum() )
        return s == s[::-1]




print(Solution().isPalindrome("A man, a plan, a canal: Panama"))