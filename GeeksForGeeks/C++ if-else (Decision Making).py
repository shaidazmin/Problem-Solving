#User function Template for python3
class Solution:
    def compareFive (ob,N):
        if N == 5:
            return 'Equal to 5'
        elif N < 5:
            return 'Less than 5'
        else:
            return 'Greater than 5'
        
print(Solution().compareFive(8))

