class Solution:
    def shortest_palindrome(self, str):
        for index, s in enumerate(str):
            if index %2 != 0 and not s.isupper() or index %2 == 0 and not s.islower():
                return 'No'
        return 'Yes'    
# s = 'S'
# print(not s.isupper())

s = input()
print(Solution().shortest_palindrome(s))        