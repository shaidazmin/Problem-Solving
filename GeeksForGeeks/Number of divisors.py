class Solution:
    def count_divisors(self, N):
        count = 0
        limit = int(N ** 0.5) 
        for i in range(1,limit+1):
            if N % i == 0:
                if i % 3 == 0:
                    count += 1
                if i != N // i and (N // i) % 3 == 0:
                    count += 1
        return count
print(Solution().count_divisors(10))            
