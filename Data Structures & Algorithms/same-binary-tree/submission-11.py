# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if two trees are equivalent it means the root is equivalent and the left and right subtrees are equivalent
        # base case: if both nodes are None, they are trivially equivalent - this handles both the empty tree cases and null children of leaf nodes
        if not p and not q:
            return True
        if not p or not q:
            return False
        # for any non-null p and q, we recursively compute if the left and right subtrees are equivalent then return True if the roots are equivalent
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        