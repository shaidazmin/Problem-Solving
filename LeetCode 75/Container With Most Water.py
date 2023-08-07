class Solution(object):
    def maxArea(self, height):
        # return height[len(height)-1]
        l, max = len(height) - 1, 0
        for i in range(len(height)):
           print(i)
           print(min(height[i],(height[l])), l-i+1)
           max = min(height[i],(height[l])) * l-i
        #    l-=1
        return max

# print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,2,1]))