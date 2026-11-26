class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i, num in enumerate(nums):
            numToIndex[num] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numToIndex and numToIndex[diff] != i:
                return [i, numToIndex[diff]]