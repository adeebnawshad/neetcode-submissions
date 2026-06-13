class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)] # we take the extra one because we need i + 1 and j + 1 in our calculation
        
        dp[m - 1][n - 1] = 1 # set destination to 1 as only one way to reach it from itself
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1] # += is for the destination cell

        return dp[0][0]