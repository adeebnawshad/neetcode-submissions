class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)] # dp[i][j] = LCS(text1[:i], text2[:j])
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1): # we're checking all j for i = 1, then all j from i = 2, ... so we are checking every combination
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 # because of the -1 we can't start at 0 so we need the extra 1 in the dp array
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # if text1[i - 1] and text2[j - 1] don't match, the LCS(text1[:i], text2[:j]) must come from one of two smaller subproblems (might not use text[i - 1] or might not use text[j - 1]) # see line 5 if confused
        return dp[len(text1)][len(text2)] 