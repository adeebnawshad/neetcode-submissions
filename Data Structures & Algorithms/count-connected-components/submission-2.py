class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        numComponents = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        for node in range(n):
            if node not in visited: # found a node that was never reached by previous DFS traversals
                dfs(node)
                numComponents +=1
        return numComponents