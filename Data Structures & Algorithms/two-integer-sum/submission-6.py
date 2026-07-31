class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i, num in enumerate(nums):
            numToIndex[num] = i
        for i in range(len(nums)):
            value = target - nums[i]
            if value in numToIndex and numToIndex[value] != i:
                return [i, numToIndex[value]]
                