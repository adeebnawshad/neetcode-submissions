class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash_table = {}
        for char in s:
            if char in s_hash_table:
                s_hash_table[char] += 1
            else:
                s_hash_table[char] = 1
        for char in t:
            if char not in s_hash_table:
                return False
            else:
                s_hash_table[char] -= 1
            if s_hash_table[char] < 0:
                return False
        return True
            