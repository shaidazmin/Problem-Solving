class Solution:
    def shortest_palindrome(self, A, B):
        A = [s for s in A]
        A.sort()
        B = [s for s in B]
        B.sort()
        return 'YES' if A == B else 'NO'
        
A = input()
B = input()
print(Solution().shortest_palindrome(A,B))