# Probelm URL 
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):
        newArray = []
        for i in nums:
            if i not in newArray:
                newArray.append(i)
        return len(newArray)