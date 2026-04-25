class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        l = 0
        subArraySum = 0
        for r in range(len(nums)):
            subArraySum += nums[r]
            while subArraySum >= target:
                minLength = min(r - l + 1, minLength)
                subArraySum -= nums[l]
                l += 1
        if minLength == float('inf'):
            return 0
        return minLength