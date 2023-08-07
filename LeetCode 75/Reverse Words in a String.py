class Solution(object):
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])

print(Solution().reverseWords("the sky is blue"))        