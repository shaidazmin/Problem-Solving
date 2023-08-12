class Solution:
	def reverse_digit(self, n):
		return int(str(n)[::-1])

print(Solution().reverse_digit(122))