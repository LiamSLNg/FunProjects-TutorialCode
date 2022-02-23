from pprint import pprint

def find_next_empty(puzzle):
    for rw in range(9):
        for cl in range(9):
            if puzzle[rw][cl] == -1:
                return rw, cl
    
    return None, None

def is_valid(puzzle, guess, row, col):
    row_values = puzzle[row]
    if guess in row_values:
        return False
    
    col_values = []
    for i in range(9):
        col_values.append(puzzle[i][col])
    if guess in col_values:
        return False
    
    #Check the 3x3 squares
    row_start = (row//3) * 3
    col_start = (col//3) * 3

    for rw in range(row_start, row_start + 3):
        for cl in range(col_start, col_start + 3):
            if puzzle[rw][cl] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    #Choose position on the board to make a guess
    row, col = find_next_empty(puzzle)

    #If there is no one else
    if row is None:
        return True
    
    #There is someone
    for guess in range(1, 10):
        #Check if guess is valid
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            #recursively call solve function
            if solve_sudoku(puzzle):
                return True
        #backtrack - change the past
        puzzle[row][col] = -1

    #No solution - can't be the code - Fail
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
