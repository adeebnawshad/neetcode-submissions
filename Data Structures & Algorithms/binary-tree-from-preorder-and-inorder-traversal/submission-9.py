# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorderIdx = 0
        inorderIndices = {}
        for i, num in enumerate(inorder):
            inorderIndices[num] = i
        def build(l, r):
            if l > r:
                return
            nonlocal preorderIdx
            rootVal = preorder[preorderIdx]
            rootIdx = inorderIndices[rootVal]
            root = TreeNode(rootVal, None, None)
            preorderIdx += 1
            root.left = build(l, rootIdx - 1)
            root.right = build(rootIdx + 1, r)
            return root
        return build(0, len(inorder) - 1)
