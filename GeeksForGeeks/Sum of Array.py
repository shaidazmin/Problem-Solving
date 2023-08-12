class Solution:
	def _sum(self,arr, n):
		res = 0
		for i in range(n):
			res += arr[i]
		return res	
	
print(Solution()._sum([1, 2, 3, 4], 4))    
