class Solution:
    def gcd(self, A, B):
        # code here
        divident = max(A, B)
        divisor = min(A, B)
        rem = 1
        while rem != 0:
            rem = divident%divisor
            divident = divisor
            divisor = rem
        return divident

print(Solution().gcd(60,24))