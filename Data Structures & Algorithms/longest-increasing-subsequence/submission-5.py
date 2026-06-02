class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        dp = [1] * len(nums)
        if nums[1] > nums[0]:
            dp[1] = 2
        for i in range(2, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1) # dp[i] stores the length of the LIS ending at nums[i], not within nums[0: i + 1]
        return max(dp)
