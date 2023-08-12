class Solution:
    def printTillN(self, N):
        if N != 0:
            self.printTillN(N-1)
            print(N, end=' ')

print(Solution().printTillN(10))            