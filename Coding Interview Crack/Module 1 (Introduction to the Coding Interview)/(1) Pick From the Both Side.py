# Problem URL 
# https://www.interviewbit.com/problems/pick-from-both-sides/


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)

        # Initialize the initial sum and maximum sum
        initial_sum = sum(A[:B])
        max_sum = initial_sum

        # Use a sliding window to find the maximum sum
        left_ptr = B - 1
        right_ptr = n - 1

        while left_ptr >= 0:
            initial_sum = initial_sum - A[left_ptr] + A[right_ptr]
            max_sum = max(max_sum, initial_sum)
            left_ptr -= 1
            right_ptr -= 1

        return max_sum
