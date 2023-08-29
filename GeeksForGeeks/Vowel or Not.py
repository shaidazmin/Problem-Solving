#User function Template for python3
class Solution:
    def isVowel (ob,c):
        vowel = ['a', 'e', 'i', 'o', 'u']
        return 'YES' if c in vowel else 'NO'
    
print(Solution().isVowel('a'))    