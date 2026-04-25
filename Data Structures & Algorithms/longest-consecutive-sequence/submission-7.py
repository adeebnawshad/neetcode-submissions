class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        if len(nums) == 0:
            return 0
        longest = 1

        for num in numsSet:
            if (num - 1) not in numsSet:
                number = num
                tempLong = 1
                number += 1
                while number in numsSet:
                    number += 1
                    tempLong += 1
                    longest = max(longest, tempLong)
        return longest