class Solution:
    def shortest_palindrome(A, B):
        return B+A

A,B = map(str, input().split())
print(Solution.shortest_palindrome(A,B))        