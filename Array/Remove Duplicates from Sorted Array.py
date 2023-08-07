class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        j = 0
        if len(A)<1:
            return j
        for i in range(1, len(A)):
            print(i)
            if A[i] != A[j]:
                j+=1
                A[j] = A[i]  
        
        return j+1

Solution().removeDuplicates([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ])