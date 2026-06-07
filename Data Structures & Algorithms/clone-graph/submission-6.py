"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # The key challenge here is that graphs can have cycles
        # — if I just recursively copy each node's neighbors, I'd loop forever.
        # So I need a way to track which nodes I've already cloned. 
        # I'll use a hashmap from original node → cloned node.
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node] # this handles cycles and avoids re-processing.
            
            copy = Node(node.val, None) # create a copy with neighbors as Node
            oldToNew[node] = copy # add to the hashmap before recursing
            for nei in node.neighbors: # then recursively clone each neighbor and append to the clone's neighbor list.
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None # return the result of the DFS if node is not NULL or else just return None