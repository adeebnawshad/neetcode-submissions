class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # first reverse the matrix vertically (just reverse the list)
        matrix.reverse()
        # now transpose the matrix
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
