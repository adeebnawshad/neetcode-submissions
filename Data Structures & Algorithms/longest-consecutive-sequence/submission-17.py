class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for num in numSet:
            if (num - 1) not in numSet:
                i = num + 1
                count = 1
                while i in numSet:
                    i += 1
                    count += 1
                longest = max(count, longest)
        return longest