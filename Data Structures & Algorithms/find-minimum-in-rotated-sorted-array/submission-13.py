class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
                mid = (l + r) // 2
                if nums[mid] > nums[r]: # min lies in right sorted array
                        l = mid + 1
                else:
                        r = mid # min lies in left sorted array
        return nums[l]

                
            