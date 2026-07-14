class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        # [3, 4, 5, 6, 1, 2]
        while l < r:
            mid = (l + r) // 2
            # if mid > r:
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]