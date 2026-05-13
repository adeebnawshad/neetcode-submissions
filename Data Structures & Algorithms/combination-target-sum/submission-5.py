class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(i, total, path):
            if total == target: # base case
                res.append(path.copy()) # save answer
                return

            if i >= len(nums) or total > target:
                return
                
            path.append(nums[i]) # make choice
            dfs(i, total + nums[i], path) # backtrack (updated state) (recursive call) - for the same number as repeats allowed
            path.pop() # undo the choice so other paths can be explored
            dfs(i + 1, total, path) # backtrack (updated state) (recursive call) - try the next number after undoing
        dfs(0, 0, [])
        return res