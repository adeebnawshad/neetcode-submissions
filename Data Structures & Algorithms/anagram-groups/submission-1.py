class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams (use this function so we don't need to deal with the edge case where count not in res)
        for s in strs:
            count = [0] * 26 # a ... z 

            for c in s:
                count[ord(c) - ord("a")] += 1 # a = 80, b = 81, ...
            
            res[tuple(count)].append(s) # lists cannot be key in python so change to tuple as tuples are non-mutable

        return res.values()