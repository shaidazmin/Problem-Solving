
class Solution:    
    #Complete this function
    def printNos(self,N):
        # print(N,"\n")
        if(N>0):
            print(N,end=' ', )
            self.printNos( N -1 )
            print(N,end=' ')
        
            

print(Solution().printNos(10))