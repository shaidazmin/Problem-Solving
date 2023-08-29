class Solution:
    def count (self,s):
        up,lw,nm,sp = 0,0,0,0
        for i in s:
            if  i.isupper():
                up+=1
            elif i.islower():
                lw+=1
            elif i.isnumeric():
                nm+=1
            else:
                sp+=1          
        return [up, lw, nm, sp]     

print(Solution().count("#GeeKs01fOr@gEEks07"))