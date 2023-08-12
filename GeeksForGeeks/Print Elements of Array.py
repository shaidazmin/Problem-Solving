class Solution:
    # Just print the space seperated array elements
	def printArray(self,arr, n):
		for i in range(n):
		    print(arr[i],end=' ')
		
print(Solution().printArray([1, 2, 3, 4, 5], 5))        