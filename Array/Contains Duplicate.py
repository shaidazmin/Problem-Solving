class Solution(object):
    def containsDuplicate(nums):
        nums.sort()
        j = 0
        for i in range(1, len(nums)):
            if nums[j] == nums[i]:
                return True
            j+=1
        return False    


print(Solution.containsDuplicate( [1,2,3,1]))        