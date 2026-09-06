class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def is_duplicate(groups):
            for group in groups:
                for c in group:
                    if c != "." and group.count(c) > 1:
                        return False
            return True

        # 横
        board1 = board
        # 縦
        board2 = [[0] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                board2[i][j] = board[j][i]

        # マス目
        board3 = []
        for i in range(3):
            for j in range(3):
                board3.append([x for row in board[3*i:3*i+3] for x in row[3*j:3*j+3]])

        return is_duplicate(board1) and is_duplicate(board2) and is_duplicate(board3)