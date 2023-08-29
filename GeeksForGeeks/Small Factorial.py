class Solution:
	def find_fact(self, n):
		if n == 0:
			return 1
		else:
			def fact(n):
				return n * (n-1)
		return fact(n)	
print(Solution().find_fact(5))	