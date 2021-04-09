# 1.8 Zero Matrix

# Write an algorithm such that if and element in an M x N matrix
# is 0, its entire row and column are set to 0.

from copy import copy, deepcopy

# The following solution has a runtime of O(NM) which is the
# best that can be done since any algorithm must touch all
# the elements in the NxM matrix

# We store the i index and the j index where the 0 was found
# in a set so we avoid replacing rows and columns that were
# already zero.

# Finally, we iterate over the index for i and j, and we replace
# the rows and columns for zero.

def zero_matrix(mat):
    i_list = set()
    j_list = set()
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if(mat[i][j] == 0):
                i_list.add(i)
                j_list.add(j)
    
    for i_index in i_list:
        for j in range(len(mat[i_index])):
            mat[i_index][j] = 0
    
    for j_index in j_list:
        for i in range(len(mat[j_index])):
            mat[i][j_index] = 0

    return mat

# Test cases:

mat1 = [
    [1,2,3],
    [4,0,6],
    [7,8,9]
]

mat2 = [
    [0,2,3],
    [4,5,6],
    [7,8,0]
]

ans1 = zero_matrix(mat1)
ans2 = zero_matrix(mat2)

for row in ans1:
    print(row)

print()

for row in ans2:
    print(row)