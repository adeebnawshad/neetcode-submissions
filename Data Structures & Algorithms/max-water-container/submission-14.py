class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            res = max(res, min(heights[r],heights[l]) * (r - l))
            if heights[l] < heights[r]:
                # area limited by heights[l] so if we move r, it'll become either still limited by l or something smaller, with 1 less width
                l += 1
            else:
                r -= 1
        return res