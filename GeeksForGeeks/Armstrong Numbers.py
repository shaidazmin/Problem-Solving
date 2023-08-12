class Solution:
    def armstrongNumber (self, n):
        s = str(n)
        result = 0
        for i in s:
            result += int(i) * int(i) * int(i)
        return 'Yes' if n == result else 'No'

print(Solution().armstrongNumber(153))        