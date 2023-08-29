class Solution:
	def sum_of_square_evenNumbers(self, n):
		# Easy Solution with O(1) time complexity 

		# return ((2*n)*(n+1)*(2*n+1))//3
        
        #Bruiteforce Solution with O(n) time complexity 
		total = 0
		num = 2
		for i in range(1, n+1):
			total += num * num
			num = num + 2
		return total
	
	
	


print(Solution().sum_of_square_evenNumbers(3))