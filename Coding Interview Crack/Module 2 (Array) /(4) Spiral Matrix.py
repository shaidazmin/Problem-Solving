# Problem URL 
# https://leetcode.com/problems/spiral-matrix/

# Notes
# Flag
# top = 0, down = len(matrix), left = 0, right = len(matrix)
# direction are 0 = left to right, 1 = top to down, 2 = right to left, 3 = down to top


class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        result = []
        rows, cols = len(matrix), len(matrix[0])
        top, down, left, right = 0, rows, 0, cols
        direction = 0

        while top < down and left < right:
            if direction == 0:
                for j in range(left, right):
                    result.append(matrix[top][j])
                top += 1
            elif direction == 1:
                for i in range(top, down):
                    result.append(matrix[i][right - 1])
                right -= 1
            elif direction == 2:
                for j in range(right - 1, left - 1, -1):
                    result.append(matrix[down - 1][j])
                down -= 1
            else:
                for i in range(down - 1, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
            
            direction = (direction + 1) % 4

        return result




print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))