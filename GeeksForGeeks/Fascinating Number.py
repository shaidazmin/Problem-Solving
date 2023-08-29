#User function Template for python3
class Solution:

	def fascinating(self,n):
		fascinating_arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
		a  = str(int(n * 2)) + str(int( n * 3)) + str(n)
		a = [n for n in a]
		a.sort()
		print(a)
		
		return a == fascinating_arr

print(Solution().fascinating(879))    
	