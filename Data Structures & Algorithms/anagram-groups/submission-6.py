class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            # count frequency of each character a-z using an array of size 26
            # then use that tuple(array) as a key to a hashmap to map the frequencies to the list of strings
            res = defaultdict(list)
            for s in strs:
                count = [0] * 26
                for c in s:
                    count[ord(c) - ord('a')] += 1
                res[tuple(count)].append(s)
            return list(res.values())