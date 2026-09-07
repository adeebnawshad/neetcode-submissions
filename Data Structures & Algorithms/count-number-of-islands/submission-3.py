class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # do dfs from each cell
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r, c):
            # base case / negative cases
            if r >= ROWS or c >= COLS or min(r, c) < 0 or (r,c) in visited or grid[r][c] == "0":
                return

            visited.add((r,c))

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands
