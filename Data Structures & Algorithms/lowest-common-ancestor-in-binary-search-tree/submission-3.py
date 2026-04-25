# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(root, node):
            if not root and node:
                return False
            if root.val == node.val:
                return True
            return search(root.left, node) or search(root.right, node)
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        if (search(root.left, p) and not search(root.left, q)) or (search(root.left, q) and not search(root.left, p)):
            return root
        elif search(root.left, p) and search(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
            
