
class Solution:
    def longest(self, arr, n):
        sln = 1
        for i in arr:
            sln *= i
        return sln


print(Solution().longest([1, 2, 3, 4, 5], 5))