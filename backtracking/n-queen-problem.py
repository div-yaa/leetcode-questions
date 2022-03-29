# leetcode question: https://leetcode.com/problems/n-queens/
from typing import List, Set

def solve_n_queens(n: int) -> List[List[str]]:
    def generate_solution(board: List[List[str]]) -> List[str]:
        result = []
        for i in range(n):
            result.append(''.join(board[i]))
        return result

    def add_queen(row: int, cols: Set[int], diags: Set[int], adiags: Set[int], board: List[List[str]]):
        if row == n:
            ans.append(generate_solution(board))
            return
        
        for col in range(n):
            diag = row - col
            adiag = row + col
            if col in cols or diag in diags or adiag in adiags:
                continue
            cols.add(col)
            diags.add(diag)
            adiags.add(adiag)
            board[row][col] = 'Q'
            add_queen(row + 1, cols, diags, adiags, board)
            cols.remove(col)
            diags.remove(diag)
            adiags.remove(adiag)
            board[row][col] = '.'

    ans = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    add_queen(0, set(), set(), set(), board)
    return ans


print(solve_n_queens(4))