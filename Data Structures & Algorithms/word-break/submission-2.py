class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # need to cover whole string
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        # Start from last character and check if the remaining portion matches a word from wordDict
        for i in range(len(s) - 1, -1, -1): # then move back by 1 until index 0
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]
        # dp[len(s)] = True
        # dp[0] = dp[0 + len(w)]  # len(w) is the length of the word in wordDict we were able to match at dp[0]