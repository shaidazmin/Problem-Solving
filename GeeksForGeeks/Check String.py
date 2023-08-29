class Solution:
    def check (self,s):
        ch = s[0]
        for c in s:
            if ch != c:
                return False
        return True
    