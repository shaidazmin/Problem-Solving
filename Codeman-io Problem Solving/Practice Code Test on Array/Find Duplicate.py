class Solutions:
    def find_duplicate(self, nums):
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen.add(nums[i])

print(Solutions().find_duplicate([1, 6,2, 3,4, 2, 8]))    

# N = int(input())
# nums = list(map(int, input().split()))[:N]
# print(Solutions().find_duplicate(nums))    