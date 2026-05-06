class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit, prevHeight):
            # stop if invalid conditions (need to check if (r,c) in visit to avoid redoing the dfs (infinite loops))
            if (r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight:
                return
            # add to visit array (pacific or atlantic)
            visit.add((r, c))

            # recursive calls on neighbors
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        # find cells that flow to each border
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c]) # first row
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c]) # last row

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0]) # first column
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1]) # last column

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r,c) in atlantic:
                    res.append([r, c])
        return res