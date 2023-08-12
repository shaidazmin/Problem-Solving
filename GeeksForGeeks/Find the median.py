class Solution:
	def find_median(self, v):
		v.sort()
		n = len(v)
		index = n//2
		if n % 2 !=0:
			return v[index]
		return ( v[index-1] + v[index] ) // 2

print(Solution().find_median([56, 67, 30, 79]))        