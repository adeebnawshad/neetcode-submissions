class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #AAABABB, k = 1
        l = 0
        res = 0
        count = {}
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k: # no need for while as r only going up 1 at a time (but while works too)
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res