def solve_n_queens(n):
    """
    Solve the n-queens problem using backtracking with branch and bound.
    Returns a list of solutions, where each solution is represented as a list
    of integers. Each integer indicates the column position of the queen in the corresponding row.
    """
    solutions = []
    # board[i] is the column where the queen is placed in row i
    board = [-1] * n

    # Helper arrays for branch and bound
    columns = [False] * n          # True if a queen occupies that column
    # True if a queen occupies the (row+col) diagonal
    diag1 = [False] * (2 * n - 1)
    # True if a queen occupies the (row-col+n-1) diagonal
    diag2 = [False] * (2 * n - 1)

    def backtrack(row):
        # All queens have been placed
        if row == n:
            solutions.append(board.copy())
            return

        # Try every column in the current row
        for col in range(n):
            # Check the branch (bound) conditions using the helper arrays.
            if not columns[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                # Place the queen
                board[row] = col
                columns[col] = True
                diag1[row + col] = True
                diag2[row - col + n - 1] = True

                # Move on to place queen in the next row
                backtrack(row + 1)

                # Backtrack: remove the queen and unmark the constraints
                columns[col] = False
                diag1[row + col] = False
                diag2[row - col + n - 1] = False

    backtrack(0)
    return solutions


# Example usage:
if __name__ == '__main__':
    n = 8  # Change n to solve for different board sizes
    solutions = solve_n_queens(n)
    print(f"Total solutions for {n}-queens: {len(solutions)}")
    # Print the first solution in a human-readable format
    if solutions:
        first_solution = solutions[0]
        for row in range(n):
            line = ['.'] * n
            line[first_solution[row]] = 'Q'
            print(" ".join(line))
