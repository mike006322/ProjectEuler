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
    grid = [[8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
            [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00],
            [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
            [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
            [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
            [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
            [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
            [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
            [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
            [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
            [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
            [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
            [86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
            [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
            [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
            [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
            [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
            [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
            [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
            [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
    # grid = []
    # for grid_i in range(20):
    #     grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    #     grid.append(grid_t)
    print(largest_product_in_a_grid(grid))
