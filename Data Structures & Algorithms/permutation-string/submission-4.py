class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1freq = [0] * 26
        s2subfreq = [0] * 26
        for char in s1:
            s1freq[ord(char) - ord('a')] += 1
        for i in range(len(s1)):
            s2subfreq[ord(s2[i]) - ord('a')] += 1
        if s2subfreq == s1freq:
            return True
        l = 0
        r = len(s1) # next character to add
        while r < len(s2):
            s2subfreq[ord(s2[l]) - ord('a')] -= 1
            s2subfreq[ord(s2[r]) - ord('a')] += 1
            if s2subfreq == s1freq:
                return True
            l += 1
            r += 1
        return False
        
            