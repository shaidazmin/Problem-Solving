class Solution:
    def getSum(self, arr1, arr2):
        result = [[0 for x in range(2)] for j in range(2)]
        print(result)
        for row in range(len(arr1)):
            for col in range(len(arr1)):
                print(arr1[row][col], end=' ')
            
            print()    

arr1=[[23,43,12],[43,13,55],[23,12,13]]
arr2=[[23,43,12],[43,13,55],[23,12,13]]
arr3=[[23,43,12],[43,13,55],[23,12,13]]
arr4=[[23,43,12],[43,13,55],[23,12,13]]


print(Solution().getSum(arr1, arr2))