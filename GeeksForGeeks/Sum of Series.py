
class Solution:
	def seriesSum(self,n):
          # O(n) Complexity
          
		# res=0
		# for i in range(1,n+1):
		# 	res= res + i
		# return res

        # O(1) Complexity
        return (n * (n+1)) // 2
	

print(Solution().seriesSum(5))        