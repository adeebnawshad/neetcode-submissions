# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # max depth of a tree can be defined in terms of the max depth of its subtrees. If I know the depth of the left subtree and the depth of the right subtree, the depth of the whole tree is just 1 (for the current node) plus whichever subtree is deeper."
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return 1 + max(leftDepth, rightDepth)

        #3. Define the base case
#"Since I'm recursing down toward the leaves, I need a stopping condition. The natural base case is: if the node is None, its depth is 0. That handles both empty trees and the null children of leaf nodes."

#4. Define the recursive case
#"For any non-null node, I recursively compute the depth of the left and right subtrees, then return 1 + max(left, right). The +1 accounts for the current node itself."