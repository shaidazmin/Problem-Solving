class Solution:
    def compareNM(self, n : int, m : int) -> str:
        if n == m:
            return 'equal'
        if n < m:
            return 'lesser'
        else:
            return 'greater'


print(Solution().compareNM(4,8))