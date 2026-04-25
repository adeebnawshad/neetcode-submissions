class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin = 1
        curMax = 1
        for i in range(0, len(nums)):
            temp = curMax * nums[i]
            curMax = max(temp, nums[i], curMin * nums[i])
            curMin = min(temp, nums[i], curMin * nums[i])
            res = max(res, curMax)
        return res
            