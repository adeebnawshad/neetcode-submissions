class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            most = max(most, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return most