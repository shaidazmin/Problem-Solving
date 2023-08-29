
class Solution:
	def streamAvg(self, arr, n):
		res = 0 
		res = 0 
		final_result = []
		for i in range(len(arr)):
			res += arr[i]
			final_result.append(round(res / (i+1), 2))
		return 	final_result
		    



print(Solution().streamAvg([10, 20, 30, 40, 50],5))
