# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = 0
        indices = {} # inorder value to index
        for i, num in enumerate(inorder):
            indices[num] = i
        def dfs(l, r):
            if l > r:
                return
            nonlocal preIdx
            rootVal = preorder[preIdx]
            preIdx += 1
            root = TreeNode(rootVal, None, None)
            mid = indices[rootVal]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder) - 1)