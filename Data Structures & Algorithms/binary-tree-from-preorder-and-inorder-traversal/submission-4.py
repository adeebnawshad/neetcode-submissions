# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorderIdx = 0
        inorderNumToIndex = {}
        for (i, num) in enumerate(inorder):
            inorderNumToIndex[num] = i
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.preorderIdx]
            self.preorderIdx += 1
            root = TreeNode(root_val, None, None)
            mid = inorderNumToIndex[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(preorder) - 1)
        