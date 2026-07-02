class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                count = 1
                i = num
                while (i + 1) in numSet:
                    count += 1
                    i += 1
                longest = max(longest, count)
        return longest