from operator import mul
from functools import reduce

class Solution:
	# @param A : list of integers
	# @return an integer
    
	def maxp3(self, A):
		A.sort()
		return max( reduce(mul, A[-3:]), reduce(mul, A[:1] + A[-2:]))
	
print(Solution().maxp3([ 0, -1, 3, 100, 70, 50 ]))