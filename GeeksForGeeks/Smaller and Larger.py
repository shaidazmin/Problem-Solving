#User function Template for python3
class Solution:
	def getMoreAndLess(self,arr, n, x):
		s = 0 
		l = 0
		for i in arr:
			if x > i:
				s += 1
			elif x < i:
				l+= 1
			elif x == i:
				s += 1
				l += 1
		return [s, l]
	
print(Solution().getMoreAndLess([1, 2, 8, 10, 11, 12, 19], 7, 0))    
				