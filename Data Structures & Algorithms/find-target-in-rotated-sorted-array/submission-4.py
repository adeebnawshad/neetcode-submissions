class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find index of minimum / deflection point
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # right sorted array has smaller values if the array has been rotated
            # if mid belongs to the left sorted array, then the minimum is somewhere to the right of mid
            # if mid belongs to the right sorted array, then the minimum is somwhere in mid or the left of mid
            
            # check if array is rotated and mid belongs to the left sorted array
            if nums[mid] > nums[r]:
                # the minimum is somewhere to the right of mid
                l = mid + 1
            else:
                r = mid
        deflectionIdx = l # or r as l == r at the end because l <= r after all conditions

        # perform binary search on the two sorted parts
        def binarySearch(l, r, target):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        left_result = binarySearch(0, deflectionIdx - 1, target)
        if left_result != -1:
            return left_result
        return binarySearch(deflectionIdx, len(nums) - 1, target)

