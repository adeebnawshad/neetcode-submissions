# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # both on left
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            # both on right
            elif p.val > node.val and q.val > node.val:
                node = node.right
            # on different sides
            else:
                return node