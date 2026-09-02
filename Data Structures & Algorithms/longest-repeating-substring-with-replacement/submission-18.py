class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        maxf = 0
        freq = {}
        # ABAA, k = 0
        # longest = 2
        l = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0) # {A : 1}
            maxf = max(freq[s[r]], maxf)
            while (r - l + 1) - maxf > k: # 7 - 4 = 3
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
