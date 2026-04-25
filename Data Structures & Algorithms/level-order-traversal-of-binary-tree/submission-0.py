# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque() # gives us a queue
        result =[]
        q.append(root)
        while q:
            qLen = len(q) # ensures we go through one level at a time
            level = []
            for _ in range(qLen):
                node = q.popleft() # first in, first out
                if node: # node could be null
                    level.append(node.val)
                    q.append(node.left) # null checks for these are done on the next iteration
                    q.append(node.right)
            if level:
                result.append(level)
        return result