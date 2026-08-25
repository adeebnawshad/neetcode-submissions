# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # try properly understanding time complexity
        # try using stack
        count = 0
        res = 0
        def inorder(root):
            if not root:
                return
            nonlocal count, res
            inorder(root.left)
            if count == k:
                return
            count += 1
            if count == k:
                res = root.val
                return
            inorder(root.right)
        inorder(root)
        return res