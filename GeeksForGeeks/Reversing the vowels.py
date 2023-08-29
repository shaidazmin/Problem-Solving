class Solution:
    def modify(self, s):
        vowels = 'a, e, i, o, u'
        find_vowel = []
        k = 0
        for index, i in enumerate(s):
            if i in vowels:
                find_vowel.append(i)
                # print(i)
        # print(find_vowel)
        print(find_vowel[::-1][k])
        res = ''
        for index, j in enumerate(s):
            res+=j  
            if j in find_vowel:
                res = find_vowel[::-1][k]
                # print(res)
                # print(j)
                k+=1
              
        print(res)    
        return find_vowel
    
print(Solution().modify("practice"))