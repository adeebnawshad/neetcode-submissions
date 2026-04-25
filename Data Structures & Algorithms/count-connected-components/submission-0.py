class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)] # create adjacency list where adj[i] is the list of nodes connected to node i - initially empty
        visited = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for adjNode in adj[node]:
                if not visited[adjNode]:
                    visited[adjNode] = True
                    dfs(adjNode)

        numComponents = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                numComponents += 1
        return numComponents