class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, path, total):
            # base case
            if total == target:
                res.append(path.copy())
                return
            # negative case
            if i >= len(nums) or total > target:
                return
            # make a choice
            path.append(nums[i])
            # choose same number again
            dfs(i, path, total + nums[i])
            # undo and choose a different number
            path.pop()
            dfs(i + 1, path, total)         
        dfs(0, [], 0)
        return res