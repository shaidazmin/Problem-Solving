class Solution:
    def findIndex (self,a, N, key ):
        #code here.
        i = 0
        index = []
        while i < N:
            if a[i] == key:
                index.append(i)
            i+=1  
        if index:
            if len(index) == 1:
                return [index[0], index[0] ]
            return [index[0], index[len(index)-1]]
        return [-1 , -1]



print(Solution().findIndex([1, 2, 5, 3, 4,  5], 6, 5))
# print(Solution().findIndex([ 6, 5, 4, 3, 1, 2], 6, 4))

