class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(row, col, i): # explore all paths from a cell   # i is the index of the current character in word
            # base case
            if i == len(word): # means we finished upto len(word - 1) so all the indexes matched as we did i + 1
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

        #Time: O(m · 3^n), where m = number of cells in the grid, n = len(word). 
        #We call dfs from every cell in the grid → factor of m.
#Each dfs call tries 4 neighbor directions, but after the first step, one direction always leads back to the cell we just came from (already in visited), so it returns instantly. That leaves 3 directions that can actually keep recursing, for up to n levels deep → 3^n per starting cell.

#(Strictly it's 4 · 3^(n-1) since the very first call has all 4 directions open, but that's a constant factor, so it simplifies to O(3^n).)

#Combined: O(m · 3^n).
    
    # Space: O(n) for visited set and also O(n) for the recursion call stack (one frame per character matched) so overall O(n), where n is the length of word