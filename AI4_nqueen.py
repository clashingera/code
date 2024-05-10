from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(col, row, board, n):
            tcol, trow = col, row
            # Check upper diagonal on left side
            while col >= 0 and row >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1

            col, row = tcol, trow
            # Check left side
            while col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1

            col, row = tcol, trow
            # Check lower diagonal on left side
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1
                row += 1

            return True

        def solve(col, board, n, result):
            if col == n:
                result.append(["".join(row) for row in board])
                return

            for row in range(n):
                if is_valid(col, row, board, n):
                    board[row][col] = 'Q'
                    solve(col + 1, board, n, result)
                    board[row][col] = '.'

        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        solve(0, board, n, result)
        return result

# Example usage:
solution = Solution()
n = 4
results = solution.solveNQueens(n)
for result in results:
    for row in result:
        print(row)
    print()  # Print an empty line to separate solutions
