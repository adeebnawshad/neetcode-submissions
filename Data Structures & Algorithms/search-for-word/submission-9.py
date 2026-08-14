class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r, c, i):
            # base case
            if i == len(word):
                return True
            # negative case
            if (
                r >= ROWS or
                c >= COLS or
                min(r, c) < 0 or
                word[i] != board[r][c]
                or (r, c) in visited
            ):
                return False
            
            # make a choice
            visited.add((r,c))
            res = (dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1))

            # undo choice and explore other options
            visited.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False