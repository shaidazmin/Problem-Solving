class Solution:
    def modify(self, s):
        return ''.join(str(e) for e in s.split(' '))
    
print(Solution().modify("geeks  for geeks"))    