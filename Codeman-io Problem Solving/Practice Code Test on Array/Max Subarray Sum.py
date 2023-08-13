def subArraySum(nums):
    max_sum = float('-inf')
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum = max(nums[i], cur_sum + nums[i])
        
        max_sum = max(max_sum, cur_sum)
        print(max_sum)
    return max_sum

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Find and print the maximum subarray sum
result = subArraySum(arr)
print(result)
