class Solution:
    def transform(self, s):
        return ' '.join([c.capitalize() for c in s.split()])

print(Solution().transform("i love programming"))    