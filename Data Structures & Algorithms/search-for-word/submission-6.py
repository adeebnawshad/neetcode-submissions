class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(row, col, i): # explore all paths from a cell   # i is the index of the letter in word
            # base case
            if i == len(word):
                return True
            # negative cases
            if (
                row > ROWS - 1
                or col > COLS - 1
                or row < 0
                or col < 0
                or board[row][col] != word[i]
                or (row, col) in visited
            ):
                return False

            # make a choice
            visited.add((row, col))
            # visit surrounding cells
            res = (dfs(row - 1, col, i + 1) or dfs(row + 1, col, i + 1) or dfs(row, col - 1, i + 1) or dfs(row, col + 1, i + 1))
            # undo choice and explore other options
            visited.remove((row, col))

            return res
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False