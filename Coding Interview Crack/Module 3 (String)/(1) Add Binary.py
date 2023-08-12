# Problem URL
# https://leetcode.com/problems/add-binary/

# Notes 

# 0 + 0 = 0 carry = 0
# 0 + 1 = 1 carry = 0
# 1 + 0 = 1 carry = 0
# 1 + 1 = 0 carry = 1
# 1 + 1 + 1 = 1 carry = 1


class Solution(object):
    def addBinary(self, a, b):
        carry = 0
        result = []
        i, j = len(a) - 1, len(b) - 1
        # print(i, j)
        # a, b = a[::-1], b[::-1]
        while i>=0 or j>=0 or carry:
            x = int(a[i]) if i>=0 else 0
            y = int(b[j]) if j>=0 else 0

            total = x + y + carry
            carry = total // 2
            digit = total % 2
            # print(x, y, total, carry, digit)

            i -= 1
            j -= 1

            result.insert(0, str(digit))

        return ''.join(result)
        
print(Solution().addBinary("11", "1"))
print(Solution().addBinary("1010", "1011"))


