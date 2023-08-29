class Solution:
    def isInRange (ob,N):
        number = {1:"one",2:"two", 3:'three',4:'four',5:'five',6:'six', 7:'seven', 8:'eight',9:'nine', 10:'ten'}
      
        if N in number:
            return  number[N]
            
        return 'not in range' 

            
print(Solution().isInRange(5))    