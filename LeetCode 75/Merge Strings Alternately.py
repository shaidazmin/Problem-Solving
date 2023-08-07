class Solution(object):
    def mergeAlternately(self, word1, word2):
        marged = []
        mx, mn =  max(word1,word2), min(word1,word2)
        i = 0
        while i < len(word1) and i < len(word2) :
            marged.append(word1[i])
            marged.append(word2[i])
            i+=1
        while i < len(mx):
            marged.append(mx[i])
            i+=1
        while i < len(mn):
            marged.append(mn[i])
            i+=1            
        return ''.join(marged) 
print(Solution().mergeAlternately("absdfdf","pqrs"))