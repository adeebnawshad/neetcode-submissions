class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # need to cover whole string
        # Start from last character and check if the remaining portion matches a word from wordDict
        # then move back by 1 until index 0
        # dp[len(s)] = True
        # dp[0] = dp[0 + len(w)]  # len(w) is the length of the word in wordDict we were able to match at dp[0]

        dp = [False] * (len(s) + 1) # for base case (dp[len(s)]) [we get indices 0 to len(s)]
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # check if enough space for w and if so then check if w in s
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
