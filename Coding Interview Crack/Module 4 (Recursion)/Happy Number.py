# Problem URL
# https://leetcode.com/problems/happy-number/
# Not properly understand

class Solution(object):
    def is_happy(self, n):
        def calculate_square_sum(num_str):
            return sum(int(digit) ** 2 for digit in num_str)

        seen_numbers = set()

        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = calculate_square_sum(str(n))

        return n == 1

# Test cases
print(Solution().is_happy(19))  # Output: True
print(Solution().is_happy(2))    # Output: False     