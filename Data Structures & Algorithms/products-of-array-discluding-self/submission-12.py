class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We're multiplying each element to the left and each element to the right of index i
        prefix = [1] * len(nums) # prefix[i] stores product of each element in nums to the left of i 
        suffix = [1] * len(nums) # suffix[i] stores product of each element in nums to the right of i

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]
            
        return result