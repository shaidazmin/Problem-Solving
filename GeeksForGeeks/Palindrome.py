class Solution:
	def is_palindrome(self, n):
		return 'Yes' if str(n) == str(n)[::-1] else 'No'


print(Solution().is_palindrome(555))