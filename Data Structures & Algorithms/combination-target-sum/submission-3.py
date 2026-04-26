class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, cur, sum):
            if sum == target:
                res.append(cur.copy())
            for j in range(i, len(nums)):
                if sum + nums[j] > target:
                    return # invalid path
                cur.append(nums[j])
                dfs(j, cur, sum + nums[j])
                cur.pop() # remove the last element to allow other decision trees
        dfs(0, [], 0)
        return res