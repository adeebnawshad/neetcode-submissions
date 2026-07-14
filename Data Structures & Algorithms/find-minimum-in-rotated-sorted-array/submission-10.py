class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        # [3, 4, 5, 6, 1, 2]
        # get out of the loop as soon as l == r as that is where the minimum will be
        while l < r:
            mid = (l + r) // 2
            # minimum (pivot) must be on the right if the array is rotated
            # if mid in left sorted array (nums[mid] > nums[r]), minimum (pivot) must be to the right of mid, so move left pointer to after mid
            if nums[mid] > nums[r]: # if isValid(mid)
                l = mid + 1
            # if mid is in the right sorted array, minimum(pivot) can be anywhere at or before mid (minimum is the first element in the right sorted array)
            else:
                r = mid
        return nums[l]

                
            