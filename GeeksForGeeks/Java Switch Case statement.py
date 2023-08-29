class Solution:
    def switchCase(self, choice, arr):
        # Code here
        if choice == 1:
            return 3.1416 * arr[0] * arr[0]
        elif choice == 2:
            return arr[0] * arr[1]
print(Solution().switchCase(1, [5]))