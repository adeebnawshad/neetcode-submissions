class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resStart = 0
        for i in range(len(s)):
            out = 0
            while (i-out) >= 0 and (i+out) < len(s) and s[i - out] == s[i + out]:
                if ((i + out) - (i - out) + 1) > resLen:
                    resStart = i - out
                    resLen = (i + out) - (i - out) + 1
                out += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resStart = l
                    resLen = r - l + 1
                l -= 1
                r += 1
        return s[resStart: resStart + resLen]
            
                