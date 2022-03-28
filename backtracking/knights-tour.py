# knight should visit every cell on the board

def is_move_possible(n, x, y, board):
    if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1:
        return True
    return False

def find_path(n, board, curr_x, curr_y, moves, pos):
    if pos == n*n:
        return True

    for move in moves:
        new_x = curr_x + move[0]
        new_y = curr_y + move[1]
        if is_move_possible(n, new_x, new_y, board):
            board[new_x][new_y] = pos
            if find_path(n, board, new_x, new_y, moves, pos + 1):
                return True
            # backtracking the path
            board[new_x][new_y] = -1
    return False

def print_solution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = ' ')
        print()

def knight_tour(n):
    # create board
    board = [[-1 for i in range(n)] for i in range(n)]
    # knight starts from (0,0)
    board[0][0] = 0
    possible_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    pos = 1
    if find_path(n, board, 0, 0, possible_moves, pos):
        print_solution(n, board)
    else:
        print('No solution exists')


# Time complexity: from every cell, there are 8 possible moves. pow(8, n**2)
# Space complexity: O(1) [not counting result space complexity]
knight_tour(8)