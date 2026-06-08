class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # We wanna find cells that flow to the pacific, cells that flow to the atlantic and take the cells common
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        # This DFS function adds cells to either set (pacific or atlantic)
        def dfs(r, c, ocean, prevHeight):
            # if invalid or already in set (to avoid doing the dfs again) we return immediately
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prevHeight or (r, c) in ocean:
                return
            
            ocean.add((r, c)) # need regular brackets and not square brackets because cannot use 'list' as a set element
            
            # recursive calls
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        # run DFS on first row and last row
        for i in range(COLS):
            dfs(0, i, pacific, heights[0][i]) # first row is connected to the pacific
            dfs(ROWS - 1, i, atlantic, heights[ROWS - 1][i]) # last row is connected to the atlantic

        # run DFS on first and last columns
        for i in range(ROWS):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, COLS - 1, atlantic, heights[i][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic: 
                    res.append([r, c])
        
        return res
