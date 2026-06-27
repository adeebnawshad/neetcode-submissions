class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        res = []
        for (i, num) in  enumerate(nums):
            numToIndex[num] = i
        # {3 : 0, 4 : 1, 5 : 2, 6 : 3}
        for i in range(len(nums)):
            lookFor = target - nums[i]
            if lookFor in numToIndex and numToIndex[lookFor] != i:
                res.append(i)
                res.append(numToIndex[lookFor])
                return res