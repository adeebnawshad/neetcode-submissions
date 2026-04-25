class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # replace characters with the most frequent character in the string
        res = 0
        charToFreq = {}
        mostFrequent = 0
        l, r = 0, 0
        
        while r < len(s):
            if s[r] in charToFreq:
                charToFreq[s[r]] += 1
            else:
                charToFreq[s[r]] = 1
            if r - l + 1 - max(charToFreq.values()) > k:
                charToFreq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res