# 1.7 Rotate Matrix

# Given an image represented by an N x N matrixm where each
# pixel in the image is represented by an integer, write a
# method to rotate the image by 90 degrees. Can you do this
# in place?

from copy import copy, deepcopy

# The following solution has a runtime of O(n^2) which is
# the best that can be done since any algorithm must
# touch all O(n^2) elements

def rotate_matrix(matrix):
    new_mat = deepcopy(matrix)
    
    n = len(matrix)
    down_i = n -1
    for up_i in range(n):
        for j in range(n):
            new_mat[j][down_i] = matrix[up_i][j]
        down_i-=1

    return new_mat

mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(rotate_matrix(mat))