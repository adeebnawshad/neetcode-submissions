class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                # act, pots, tops, cat, stop, hat
                # [["hat"],["act", "cat"],["stop", "pots", "tops"]]

                #(h: 1, a: 1, t: 1), (a: 1, c: 1, t: 1), ...

                countToStr = {}
                for s in strs:
                        count = [0] * 26
                        for char in s:
                                count[ord(char) - ord('a')] += 1 
                        if tuple(count) not in countToStr:
                                countToStr[tuple(count)] = []
                        countToStr[tuple(count)].append(s)

                return list(countToStr.values())
