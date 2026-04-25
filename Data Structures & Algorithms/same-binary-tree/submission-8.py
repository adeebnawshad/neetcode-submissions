# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base cases (0 nodes and 1 node)

        # both NULL - return True
        if not p and not q:
            return True
        
        # either one NULL - return False
        if not p and q:
            return False
        if p and not q:
            return False
        
        # if node values not equal, return False 
        if p.val != q.val:
            return False
        
        # recursive case: call on both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)