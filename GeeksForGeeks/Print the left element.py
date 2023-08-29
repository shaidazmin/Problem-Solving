class Solution:
    def leftElement(self, arr, n):
        arr.sort()
        if n % 2 == 0:
            return arr[(n // 2 )-1]

        return arr[(n // 2 )]
    
print(Solution().leftElement([7, 8, 3, 4, 2, 9, 5], 7))