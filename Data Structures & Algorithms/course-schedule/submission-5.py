class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # convert into adjacency list
        adjList = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            adjList[pair[0]].append(pair[1])

        path = set() # if initialized inside the dfs function, would create empty set even on recursive call so wouldn't be able to detect cycles

        def dfs(node):
            if node in path:
                return False # cycle detected
            if adjList[node] == []:
                return True # no more neighbors to check
            path.add(node)
            for nei in adjList[node]:
                if not dfs(nei): # can't do just return dfs(nei) because that would return after only checking the first neighbor in the list
                    return False
            path.remove(node) # remove node after exploring all neighbors so that future traversals don't incorrectly think there's a cycle
            adjList[node] = [] # avoids repeated DFS of nodes already verified acyclic
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True