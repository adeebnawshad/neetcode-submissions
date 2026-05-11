class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adjList = [[] for _ in range(n)]
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        visited = set()

        def dfs(node, parent): # need to keep track of parent as undirected graph, as otherwise if sees 1 in adjList of 0 and 0 in adjList of 1, will think there's a cycle
            if node in visited:
                return False

            visited.add(node)

            for nei in adjList[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True


        if not dfs(0, -1): # no need to loop as in a tree, all nodes should be connected
            return False
        return len(visited) == n # checks that all of the nodes are connected