class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            # use hashmap to map frequencies tuple to strings, e.g. {{a-1, b-0, c-1, ... t-1, ...} : "act", "cat" }
            res = defaultdict(list) # creates a hash map where the value is an empty list by default
            for s in strs:
                freq = [0] * 26
                for c in s:
                    freq[ord(c) - ord('a')] += 1
                res[tuple(freq)].append(s)
            return list(res.values())
