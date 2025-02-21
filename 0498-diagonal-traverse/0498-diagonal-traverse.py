class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])  
        ans = []  
        i, j = 0, 0 
        up = True  
        while len(ans) < rows * cols:
            ans.append(mat[i][j]) 

            if up: 
                if j == cols - 1: 
                    i += 1
                    up = False
                elif i == 0: 
                    j += 1
                    up = False
                else: 
                    i -= 1
                    j += 1
            else: 
                if i == rows - 1:  
                    j += 1
                    up = True
                elif j == 0:  
                    i += 1
                    up = True
                else:  
                    i += 1
                    j -= 1

        return ans