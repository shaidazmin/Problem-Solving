class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        j = 0  # Pointer to keep track of the last unique element
        
        for i, num in enumerate(nums[1:], start=1):
            if num != nums[j]:
                j += 1
                nums[j] = num
        
        return j + 1, nums

# Test cases
solution = Solution()

nums1 = [1, 1, 2]
print(solution.removeDuplicates(nums1))  # Output: 2, nums1 = [1, 2, _]

nums2 = [0, 0, 1, 0 ,2 , 1, 1, 2, 2, 3, 3, 4]
print(solution.removeDuplicates(nums2))  # Output: 5, nums2 = [0, 1, 2, 3, 4, _, _, _, _, _]
