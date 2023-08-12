# Problem URL
# https://leetcode.com/problems/valid-anagram/



class Solution(object):
    def isAnagram(self, s, t):
        s = [i for i in s]
        t = [i for i in t]
        s.sort()
        t.sort()
        return s == t
    

print(Solution().isAnagram("anagram", "nagaram"))    
# print(Solution().isAnagram("rat", "car"))    