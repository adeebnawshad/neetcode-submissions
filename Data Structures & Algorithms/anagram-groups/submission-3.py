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
                        # check if key already exists, create it and assign to empty list
                        if tuple(count) not in countToStr:
                                countToStr[tuple(count)] = []
                        # append s to the right list in the hashmap
                        countToStr[tuple(count)].append(s)
                # convert hashmap values into a list and return
                return list(countToStr.values())
