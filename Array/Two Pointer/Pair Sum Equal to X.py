class Solution():
    def twoSum(self, nums, target):

        stored_item = {}

        for index, num in enumerate(nums):
            
            expected_value = target - num
            print(expected_value, num)
            if expected_value in stored_item:
                return [stored_item[expected_value], index]
            stored_item[num] = index

print(Solution().twoSum([-1,-2,-3,-4,-5], -8))

        # start_index = 0
        # end_index = len(nums)-1
        # nums.sort()
        # while start_index <= end_index:
        #     print(nums[start_index] + nums[end_index], start_index, end_index)
        #     if nums[start_index] + nums[end_index] == target:
        #         return [start_index, end_index]
        #     if nums[start_index] + nums[end_index] > target:
        #         end_index-=1
        #     else:
        #         start_index+=1


              


# print(Solution().twoSum([2,7,11,15], 9))
# print(Solution().twoSum([3,2,4], 6))


# N, M = map(int, input().split())
# nums = list(map(int, input().split()))[:N]
# print(Solution().twoSum(nums,M))
