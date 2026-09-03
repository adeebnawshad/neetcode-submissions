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
            if r >= ROWS or c >= COLS or min(r, c) < 0 or (r,c) in visited or board[r][c] != word[i]:
                return
            
            # make a choice
            visited.add((r,c))
            res = dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1)
            visited.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                res = dfs(r, c, 0)
                if res:
                    return True
        return False