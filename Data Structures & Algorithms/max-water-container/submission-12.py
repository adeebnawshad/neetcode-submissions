class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]: # heights[l] is limiting the area, so if we move r, heights[l] still limits the area or something smaller limits the area, and the width decreases by 1
                l += 1
            else:
                r -= 1
        return res