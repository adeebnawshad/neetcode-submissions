class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        def dfs(row, column, i):
            if i == len(word):
                return True
            if (min(row, column) < 0 or row >= len(board) or column >= len(board[0]) or word[i] != board[row][column] or visited[row][column]):
                return False
            visited[row][column] = True
            result = (dfs(row + 1, column, i + 1) or dfs(row - 1, column, i + 1) or dfs(row, column + 1, i + 1) or dfs(row, column - 1, i + 1))
            visited[row][column] = False
            return result
        for row in range(len(board)):
            for column in range(len(board[0])):
                if dfs(row, column, 0):
                    return True
        return False
