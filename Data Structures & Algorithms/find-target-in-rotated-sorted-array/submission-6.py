class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the deflection point
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # right sorted portion has smaller elements if array is rotated
            if nums[mid] > nums[r]:
                # mid is in left sorted portion
                # so minimum is to the right of mid
                l = mid + 1
            else:
                # mid is in right sorted portion
                # so minimum is at mid or left of mid as no elements to the right of mid can be smaller than mid because of the reason in the above line
                r = mid
        deflectionPt = l

        def binary_search(l, r, target):
            while l <= r: # include equal for single element / part of algorithm when l == r, we still need to check that
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        left_result = binary_search(0, deflectionPt - 1, target)
        if left_result != -1:
            return left_result
        return binary_search(deflectionPt, len(nums) - 1, target)


