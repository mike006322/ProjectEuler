#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler011

# First I solved this for any 4 adjacent points. The question only asks for points in a straight line.

from itertools import combinations

def make_matrix(comb):
    """
    given 4 values ranging from 0 to 15 representing positions in a 4x4 grid
    return 4x4 matrix of booleans
    """
    res = [[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]]
    for i in comb:
        j = 0
        while i > 3:
            i -= 4
            j += 1
        res[j][i] = True
    return res

def matrix_embed(M):
    """
    input 4x4 matrix with booleans
    embeds into 6x6 matrix, centered, with extra values being False
    """
    M2 = M[:]
    for i in range(4):
        M2[i] = [False] + M2[i] + [False]
    res = [[False, False, False, False, False, False]] + M2 + [[False, False, False, False, False, False]]
    return res


def check_adjacency(M):
    """
    given 4x4 matrix of boolean with 4 True points
    return boolean whether the 4 True points are adjacent
    for each value check if there is one adjacent to it
    """
    # embed the 4x4 into a 6x6 matrix
    M = matrix_embed(M)
    adj = True
    for i in range(1, 5):
        for j in range(1, 5):
            if M[i][j] == True:
                point_adj = False
                for n in range(3):
                    for m in range(3):
                        if not (i == i-1+n and j == j-1+m):
                            if M[i-1+n][j-1+m] == True:
                                point_adj = True
                if point_adj == False:
                    return False
    return True


def make_shapes():
    """
    outputs a set of all shapes of four adjacent values in the form of a 4x4 boolean matrix
    """
    res = []
    values = [i for i in range(16)]
    combs = combinations(values, 4)
    for comb in combs:
        M = make_matrix(comb)
        if check_adjacency(M):
            res.append(M)
    return res


def trim_shape(shape_matrix):
    """
    input is 4x4 matricies of booleans describing shapes of four adjacent values
    return nxm matricies where each column and row has at least one True value
    """
    M = shape_matrix
    # first delete False columns then False rows
    false_columns = []
    for j in range(4):
        col_all_false = True
        for t in range(4):
            if M[t][j] == True:
                col_all_false = False
        if col_all_false:
            false_columns.append(j)
    M2 = []
    for i in range(len(M)):
        new_row = []
        for k in range(4):
            if k not in false_columns:
                new_row += [M[i][k]]
        M2.append(new_row)
    false_rows = []
    for i in range(len(M2)):
        row_all_false = True
        for k in range(len(M[i])):
            if M[i][k] == True:
                row_all_false = False
        if row_all_false:
            false_rows.append(i)
    M3 = []
    for i in range(len(M2)):
        if i not in false_rows:
            M3.append(M2[i])
    return M3

def look_for_shape(M, grid):
    """
    input is a trimmed shape
    returns maximum product of points in 20x20 grid that fit that shape
    """
    m = 0
    for i in range(21 - len(M)):
        for j in range(21 - len(M[0])):
            product = 1
            for n in range(len(M)):
                for p in range(len(M[0])):
                    if M[n][p]:
                        product *= grid[i+n][j+p]
            if product > m:
                m = product
    return m

def largest_product_in_a_grid(grid):
    # shapes = make_shapes()
    # trimmed_shapes = []
    # for shape in shapes:
    #     trimmed_shapes.append(trim_shape(shape))
    trimmed_shapes = [[[True]*4], [[True]]*4, [[True, False, False, False], [False, True, False, False], [False, False, True, False], [False, False, False, True]], [[False, False, False, True], [False, False, True, False], [False, True, False, False], [True, False, False, False]]]
    m = 0
    for shape in trimmed_shapes:
        b = look_for_shape(shape, grid)
        if b > m:
            m = b
    return m

if __name__ == '__main__':
    grid = []
    for grid_i in range(20):
        grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
        grid.append(grid_t)
    print(largest_product_in_a_grid(grid))
