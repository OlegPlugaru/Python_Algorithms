"""
Write a function that will take 3 arguments:
bombs = list of bomb locations
rows, columns
mine_sweeper([0,0], [1, 2], 3, 4)

bomb at row index 0 column index 0
bomb at row index 1 coulumn index 2
3 rows 
4 columns

we should return an 3 x 4 array (-1) = bomb
[[-1,  1,  1, 1],
[  1,  2, -1, 1],
[  0,  1,  1, 1]]
"""

def mine_sweeper(bombs, num_rows, num_cols):
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    
    for bomb_location in bombs:
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1
    
        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)

        for i in row_range:
            current_i = i
            for j in col_range:
                current_j = j
                if (0 <= current_i < num_rows and 0 <= current_j < num_cols and field[i][j] != -1):
                    field[i][j] += 1
    return field



print(mine_sweeper([[0,0],[1,2],[3,4]], num_rows=9, num_cols=9))