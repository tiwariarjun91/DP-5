# Time Complexity: O(mn)
# Space Complexity: O(mn)
# Ran on Leetcode: Yes
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)]for _ in range(m+1)]
        i = m-1
        while i>=0:
            j = n-1
            while j>=0:
                if i == m-1 and j== n-1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
                j = j-1
            i = i-1
        return dp[0][0]