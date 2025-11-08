# Design n-Queens matrix having first Queen placed. Use backtracking to place remaining Queens to generate the final n-queen’s matrix.

def print_solution(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, n):
    if col >= n:
        print_solution(board)
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, n) or res
            board[i][col] = 0
    return res

if __name__ == "__main__":
    n = int(input("Enter the size of chessboard (n): "))
    board = [[0 for _ in range(n)] for _ in range(n)]

    first_row = int(input(f"Enter the row (0 to {n-1}) to place the first Queen in column 0: "))
    board[first_row][0] = 1

    print("\nSolutions for the N-Queens problem:")
    if not solve_nqueens(board, 1, n):
        print("No solution exists.")
