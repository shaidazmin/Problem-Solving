#User function Template for python3
class Solution:
	def getBinaryRep(self, n):
		return bin(n).zfill(32).replace('0b','')
	
print(Solution().getBinaryRep(2))	