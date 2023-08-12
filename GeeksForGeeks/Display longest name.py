class Solution:
    def longest(self, names, n):
        max_len = ''
        for i in names:
            if len(max_len) < len(i):
                max_len =  i
        return max_len

print(Solution().longest(["Geek", "Geeks", "Geeksfor","GeeksforGeek", "GeeksforGeeks"], 5))