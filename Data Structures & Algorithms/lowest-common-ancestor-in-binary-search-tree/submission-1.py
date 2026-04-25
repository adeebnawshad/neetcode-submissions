# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(root, node):
            if root is None and node:
                return False
            if root.val == node.val:
                return root
            elif root.val > node.val:
                return search(root.left, node)
            else:
                return search(root.right, node)
        if root.val == p.val or root.val == q.val or p.val < root.val and q.val > root.val or q.val < root.val and p.val > root.val:
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        
            
