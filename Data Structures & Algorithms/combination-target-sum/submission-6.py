class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(i, sum, path):
            # base case
            if sum == target:
                res.append(path.copy()) # save answer # need to pass in copy as we're gonna keep updating path
                return
            # negative case
            if sum > target or i >= len(nums):
                return
            # make choice
            path.append(nums[i])
            # backtrack (updated state) (recursive call) - for the same number as repeats allowed
            dfs(i, sum + nums[i], path)
            # undo the choice so other paths can be explored
            path.pop()
            # backtrack (updated state) (recursive call) - try the next number after undoing
            dfs(i + 1, sum, path)
        dfs(0, 0, [])
        return res