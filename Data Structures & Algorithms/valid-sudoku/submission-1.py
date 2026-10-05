class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def line_check(line: List[str]) -> bool:
            count = Counter()
            for c in line:
                if c == ".":
                    pass
                else:
                    if count[int(c)] == 0:
                        count[int(c)] += 1
                    else:
                        return False
            return True
        
        check = True
        # read the boxes:
        boxes = [[0 for _ in range(9)] for _ in range(9)]
        for k in range(9):
            for i in range(3):
                for j in range(3):
                    boxes[k][3*i+j] = board[3*(k%3)+i][int(3*((k>3) and (k<=6)) + 6*(k>6)) + j]
        
        for line in boxes:
            check = check * line_check(line)
        
        for line in board:
            check = check * line_check(line)

        board_transpose = [[0 for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                board_transpose[j][i] = board[i][j]

        for line in board_transpose:
            check = check * line_check(line)

        return (check == 1)
                    
