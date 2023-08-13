def three_sum_count(arr):
    n = len(arr)
    count = 0
    
    # Sort the array to enable two-pointer approach
    arr.sort()
    
    # Fix the first element and use two-pointer approach for the remaining elements
    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            
            if total == 0:
                count += 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return count

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Count the number of indices satisfying the 3 Sum condition
result = three_sum_count(arr)
print(result)
