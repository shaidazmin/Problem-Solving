# Problem URL 
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        n, m = len(haystack), len(needle)
        for i in range(n):
            if haystack[i:i + m] == needle:
                return i
        return -1

print(Solution().strStr("sdabutsad", "sad"))
print(Solution().strStr("a", "a"))
print(Solution().strStr("hello", "ll"))
print(Solution().strStr("mississippi", "pi"))


# This was wrong Approach 


# from collections import Counter
# class Solution(object):
#     def strStr(self, haystack, needle):
#         target_value = Counter(needle)
#         extract_value = Counter(haystack[:len(needle)])
#         result = []
#         j = 1
#         for index, i in enumerate(haystack):
#             if target_value == extract_value:
#                 print((len(target_value)),target_value, extract_value, end=' : ')
#                 result.append(index)
#             extract_value = Counter(haystack[j: j+len(needle)])  
#             j+=1
#             print(index, extract_value)
#         return result[0] if result else -1