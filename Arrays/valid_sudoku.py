from collections import defaultdict
'''
Problem: Valid Sudoku
-------

You are given a `9 x 9` Sudoku board `board`. A Sudoku board is valid if the following
rules are followed:
    
    1. Each row must contain the digits `1-9` without repetition.
    2. Each column must contain the digits `1-9` without repetition.
    3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Return `true` if the Sudoku board is valid, otherwise return `false`.

Note: A board does not need to be full or be solved to be valid.

-------
URL: https://neetcode.io/problems/valid-sudoku?list=neetcode150
'''

def isValidSudoku(board: list[list[str]]) -> bool:
    # Create a dict that contains sets for rows, columns, and sections such that we can 
    # check for duplicates. We then iterate through each cell and check if that digit 
    # exists in any maps for that row/column/section. If it does, we return False.
    # If it doesn't, we add it to the corresponding map and keep building until we 
    # validate the entire board.
    
    rows_map = defaultdict(set)
    cols_map = defaultdict(set)
    sections_map = defaultdict(set)

    for col in range(9):
        for row in range(9):
            if board[col][row] == '.':
                continue
            if board[col][row] in rows_map[col] or board[col][row] in cols_map[row] or board[col][row] in sections_map[(col // 3, row // 3)]:
                return False
            
            rows_map[col].add(board[col][row])
            cols_map[row].add(board[col][row])
            sections_map[(col // 3, row // 3)].add(board[col][row])

    return True
    

    
def test1(board = 
    [["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]]):
    sol = True
    print('Test 1: PASSED' if isValidSudoku(board) == sol else 'Test 1: FAILED')
    
def test2(board =
    [["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]]):
    sol = False
    print('Test 2: PASSED' if isValidSudoku(board) == sol else 'Test 2: FAILED')
    
test1()
test2()