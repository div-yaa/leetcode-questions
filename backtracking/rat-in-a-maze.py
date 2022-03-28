# rat needs to move from source (0,0) to the destination (n-1, n-1)
# it can only move forward or downward (only 2 directions possible)
# input: a matrix with 0 and 1. 0 means a blocker, 1 means rat can pass
# through the block
# find the path
# https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/


# Time complexity: pow(2, n**n) as for every cell there are 2 moves
# Space complexity: O(1)
def rat_maze(maze):
    moves = [(1,0), (0,1)]
    maze[0][0] = -1
    if find_path(0, 0, maze, moves):
        print_solution(maze)
    else:
        print('No solution found')


def print_solution(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == -1:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()

def is_safe_move(x, y, maze):
    if x >= 0 and y >= 0 and x < len(maze) and y < len(maze[0]) and maze[x][y] == 1:
        return True
    return False

def find_path(curr_x, curr_y, maze, moves):
    if curr_x == len(maze) - 1 and curr_y == len(maze[0]) - 1:
        return True
    
    for move in moves:
        new_x = curr_x + move[0]
        new_y = curr_y + move[1]
        if is_safe_move(new_x, new_y, maze):
            maze[new_x][new_y] = -1
            if find_path(new_x, new_y, maze, moves):
                return True
            maze[new_x][new_y] = 1
    return False



maze = [ [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1] ]
rat_maze(maze)