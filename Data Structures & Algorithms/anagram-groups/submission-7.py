class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            # frequency of the characters is the same
            freqToString = defaultdict(list)
            # 1a, 1c, 1t : act, cat
            for s in strs:
                count = [0] * 26
                for c in s:
                    count[ord(c) - ord('a')] += 1
                freqToString[tuple(count)].append(s)
            return list(freqToString.values())
