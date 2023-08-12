# Problem URL 
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Buiteforce Technique 

# class Solution(object):
#     def findAnagrams(self, s, p):
#         s, p = [c for c in s], [c for c in p]
#         j = len(p)
#         p.sort()
#         result = []

#         for i in range(0, len(s)):
#             s1 = s[i:j]
#             s1.sort()
#             if s1 == p:
#                 result.append(i)
#             j+=1
#         return result

# Easy Solution 


from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):

        len_p = len(p)
        p_counter = Counter(p)
        # print(p_counter)
        s_counter = Counter(s[:len_p])
        # print(s_counter)
        result = []

        for i in range(0, len(s) - len_p + 1):
            if s_counter == p_counter:
                result.append(i)
            
            s_counter[s[i]] -= 1
            if s_counter[s[i]] == 0:
                del s_counter[s[i]]
            
            if i + len_p < len(s):  # Check if the index is within the valid range
                if s[i + len_p] in s_counter:
                    s_counter[s[i + len_p]] += 1
                else:
                    s_counter[s[i + len_p]] = 1
        
        if s_counter == p_counter:
            result.append(len(s) - len_p)
        
        return result


print(Solution().findAnagrams('cbaebabacd', 'abc'))
# print(Solution().findAnagrams('abab', 'ab'))
