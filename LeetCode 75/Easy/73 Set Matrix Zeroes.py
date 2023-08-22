#73 Set Matrix Zeroes

'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
'''


#code
#---------------------------------------------------------------------------------------------
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        arr=[]
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    arr.append([i,j])
        for k,l in arr:
            for r in range(n):
                matrix[k][r]=0
            for c in range(m):
                matrix[c][l]=0


#complexity: O(n^2)