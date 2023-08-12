# Problem URL 
# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        j = 0
        for i in range(1, len(nums)):
            if nums[j] == nums[i]:
                return True
            j+=1
        return False    
 
