class Solution:
	def removeVowels(self, S):
		vowel = ['a', 'e', 'i', 'o', 'u']
		res = ''
		for c in S:
			if c not in vowel:
				res+=c
		return res
print(Solution().removeVowels("welcome to geeksforgeeks"))