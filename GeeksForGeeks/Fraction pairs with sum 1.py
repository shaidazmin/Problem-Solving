def countFractions(N, numerator, denominator):
    fractions = [(numerator[i], denominator[i], numerator[i] / denominator[i]) for i in range(N)]
    print(fractions)
    fractions.sort(key=lambda x: x[2])
    print(fractions)
    fractions.sort()
    print(fractions)
    # left, right = 0, N - 1
    # count = 0
    
    # while left < right:
    #     if fractions[left][2] + fractions[right][2] < 1:
    #         left += 1
    #     elif fractions[left][2] + fractions[right][2] > 1:
    #         right -= 1
    #     else:
    #         count += 1
    #         left += 1
    #         right -= 1
    
    # return count

# Test cases
print(countFractions(4, [1, 2, 2, 8], [2, 4, 6, 12]))  # Output: 2
# print(countFractions(5, [3, 1, 12, 81, 2], [9, 10, 18, 90, 5]))  # Output: 2
