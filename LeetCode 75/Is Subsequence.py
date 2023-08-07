class Solution(object):
    def isSubsequence(self, s, t):
        # i, j = 0, 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i+=1
        #     j += 1    
        # return True if i == len(s) else False
        c = 0
        for j in range(len(t)):
            if c < len(s) and s[c] == t[j]:
                c+=1
        return c == len(s)





print(Solution().isSubsequence("acb","ahbgdc"))