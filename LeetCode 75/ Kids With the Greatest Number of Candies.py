class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        for i in range(len(candies)):
            if max(candies) <= candies[i]+extraCandies:
                result.append(True)
            else:
                result.append(False)
        return result
    
print(Solution().kidsWithCandies([2,3,5,1,3], 3))    
