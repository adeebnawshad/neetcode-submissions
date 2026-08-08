# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderValToIndex = {}
        for i, val in enumerate(inorder):
            inorderValToIndex[val] = i
        preIdx = 0
        def dfs(l, r):
            nonlocal preIdx
            if l > r:
                return
            rootVal = preorder[preIdx]
            preIdx += 1
            mid = inorderValToIndex[rootVal]
            root = TreeNode(rootVal, None, None)
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder) - 1)