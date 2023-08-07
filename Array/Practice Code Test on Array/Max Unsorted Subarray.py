def find_unsorted_subarray(arr):
    n = len(arr)
    
    # Find the left bound of the unsorted subarray
    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1
    if left == n - 1:
        return -1, -1  # The array is already sorted
    
    # Find the right bound of the unsorted subarray
    right = n - 1
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1
    
    # Find the minimum and maximum values within the potential unsorted subarray
    min_val = min(arr[left:right+1])
    max_val = max(arr[left:right+1])
    
    # Expand the left bound to include elements smaller than the minimum value
    while left > 0 and arr[left - 1] > min_val:
        left -= 1
    
    # Expand the right bound to include elements larger than the maximum value
    while right < n - 1 and arr[right + 1] < max_val:
        right += 1
    
    return left, right

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Find and print the start and end index of the maximum unsorted subarray
start, end = find_unsorted_subarray(arr)
print(start + 1, end + 1) if start != -1 else print(-1)
