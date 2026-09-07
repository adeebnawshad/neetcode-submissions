class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, path, sum):
            # base case
            if sum == target:
                res.append(path.copy())
                return
                
            # negative case
            if sum > target or i >= len(nums):
                return

            # make a choice
            path.append(nums[i])

            # try same number again
            dfs(i, path, sum + nums[i])

            # remove this number and then try another number
            path.pop()
            dfs(i + 1, path, sum)

        dfs(0, [], 0)
        return res


