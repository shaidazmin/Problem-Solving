class Solution:
    def countCamelCase (self,s):
        counter = 0
        for i in s:
            if i.isupper():
                counter+=1
        return counter
    
print(Solution().countCamelCase("ckjkUUYII"))