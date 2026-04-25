class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i, num in enumerate(nums):
            numToIndex[num] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numToIndex and i != numToIndex[complement]:
                return [i, numToIndex[complement]]
