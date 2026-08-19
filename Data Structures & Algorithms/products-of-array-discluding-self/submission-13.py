class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftP= [1] * len(nums) # 1, 1, 2, 8
        rightP = [1] * len(nums)

        for i in range(1, len(nums)):
            leftP[i] = leftP[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            rightP[i] = rightP[i + 1] * nums[i + 1]
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = leftP[i] * rightP[i]
        return res