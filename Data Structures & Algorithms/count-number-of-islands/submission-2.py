class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # keep a visited set to keep track
        # run dfs on each cell (keep going until all 0s) and count islands

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0
        def dfs(r, c):
            # base case
            if r >= ROWS or c >= COLS or min(r,c) < 0 or grid[r][c] == "0" or (r,c) in visited:
                return
            # or else grid[r][c] must be 1
            visited.add((r,c))
            
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:  # first check  because we don't want to count the cases where we start at a 0 and second check because we don't want to count cases where the cell is already part of an island that we counted
                    dfs(r, c)
                    islands += 1
        return islands
