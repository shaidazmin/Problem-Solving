class Solution:
    def shortest_palindrome(s):
        n = len(s)
        reversed_s = s[::-1]
        match_length = 0

        for i in range(n):
            if s[i] == reversed_s[match_length]:
                match_length += 1

        remaining_chars = reversed_s[match_length:]
        palindrome = remaining_chars + s
        return palindrome
        
s = input()
print(Solution.shortest_palindrome(s))