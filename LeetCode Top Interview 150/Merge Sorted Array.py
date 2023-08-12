class Solution(object):
    def merge(self, nums1, m, nums2, n):
        set(nums1).union(set(nums2))
        return set(nums1).intersection(set(nums2))

print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6],3))
