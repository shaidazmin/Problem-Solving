class Solution:
    def solve(self, A, B):
        sumation = sum(A[:B])
        print(sumation)
        sumation = sum(A[-B:])
        print(sumation)
        # for i in range(B):
        #     print(A[i])
        #     # sumation = sumation + A[i]


Solution().solve([5,-2,3,4,2], 3)