class Solution:
    def is_palindrome(self, str):
        return 'YES' if str == str[::-1] else 'NO'
    
str = input()
print(Solution().is_palindrome(str))    