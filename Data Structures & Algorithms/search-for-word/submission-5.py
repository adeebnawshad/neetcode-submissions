class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()

        def dfs(row, col, i):  # Explore all paths from a cell
            if i == len(word):  # found the last letter of the word, return True
                return True

            # if out of range in array or board[row][col] doesn't match word[i]
            # or already visited (in that path), discontinue that path (return False)
            if (
                min(row, col) < 0 or
                row >= len(board) or
                col >= len(board[0]) or
                word[i] != board[row][col] or
                (row, col) in path
            ):
                return False

            # otherwise add (row, col) to the path
            path.add((row, col))

            # recursively call on the surrounding cells
            res = (
                dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or
                dfs(row, col - 1, i + 1)
            )

            # remove (row, col) from path (undo to try another route)
            path.remove((row, col))

            return res
        # start from every cell
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True

        # return False after checking all cells
        return False