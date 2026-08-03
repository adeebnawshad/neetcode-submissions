class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # if array is rotated, min is in the right sorted portion
            if nums[mid] > nums[r]: # right sorted portion (so min too) is somewhere to the right of mid
                l = mid + 1
            else: # mid is in the right sorted portion so min has to be at mid or to the left of mid
                r = mid
        return nums[l]

                
            