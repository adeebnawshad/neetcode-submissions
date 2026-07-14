class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        # [3, 4, 5, 6, 1, 2]
        # get out of the loop as soon as l == r as that is where the minimum will be
        # loop invariant is min lies within nums[l..r] - the cases preserve that
        while l < r:
            mid = (l + r) // 2
            # minimum (pivot) must be on the right if the array is rotated
            # if mid in left sorted array (nums[mid] > nums[r]), minimum (pivot) must be to the right of mid, so move left pointer to after mid
            if nums[mid] > nums[r]:
                l = mid + 1
            # if mid is in the right sorted array, minimum(pivot) can be anywhere at or before mid (as minimum is the first element in the right sorted array), so move the right pointer to mid
            else: 
                r = mid
        # l == r after the while loop so can do l[r] too (as all cases preserve l <= r)
        return nums[l]

                
            