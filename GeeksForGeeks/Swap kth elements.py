#User function Template for python3
class Solution:
	
	def swapKth(self,arr, n, k):
		arr[k-1], arr[-k] = arr[-k], arr[k-1]
		return arr
		

print(Solution().swapKth([1, 2, 3, 4, 5, 6, 7, 8], 8, 3))        

# 3

# 1, 2, 3, 4, 5, 6, 7, 8
# 1, 2, 6, 4, 5, 3, 7, 8