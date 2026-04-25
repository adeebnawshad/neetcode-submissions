class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        one = 1
        two = 1
        for i in range(n - 1):
            res = one + two
            temp = one
            one = one + two
            two = temp
        return res
