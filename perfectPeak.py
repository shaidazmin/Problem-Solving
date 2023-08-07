class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):

        n = len(A)
        if n <= 2:
            return 0
        
        max_left = [0] * n
        min_right = [0] * n
        # Calculate the maximum element on the left for each position
        max_val = float('-inf')
        for i in range(n):
            max_left[i] = max_val
            max_val = max(max_val, A[i])

        # Calculate the minimum element on the right for each position
        min_val = float('inf')
        for i in range(n - 1, -1, -1):
            min_right[i] = min_val
            min_val = min(min_val, A[i])

        print(max_left)
        print(min_right)

        # Check if there exists an element that satisfies the conditions
        for i in range(1, n - 1):
            if max_left[i] < A[i] < min_right[i]:
                return 1

        return 0
        # for i in range(1, len(A) - 1):
        #     if max(A[:i]) < A[i] and min(A[i + 1:]) > A[i]:
        #         return 1
        # return 0

result = Solution().perfectPeak([9895, 30334, 17674, 23812, 20038, 25668, 6869, 1870, 4665, 27645, 7712, 17036, 31323, 8724, 28254, 28704, 26300, 25548, 15142, 12860, 19913, 32663, 32758])
print(result)  # Output: 1
