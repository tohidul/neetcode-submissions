class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = [set() for _ in range(9)]
        col_hash = [set() for _ in range(9)]
        square_hash = [set() for _ in range(9)]

        i = 0
        j = 0
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                square_hash_index = (i//3)*3 + j//3
                if val == '.':
                    continue
                if val in row_hash[i] or val in col_hash[j] or val in square_hash[square_hash_index]:
                    return False
                else:
                    row_hash[i].add(val)
                    col_hash[j].add(val)
                    square_hash[square_hash_index].add(val)

        return True