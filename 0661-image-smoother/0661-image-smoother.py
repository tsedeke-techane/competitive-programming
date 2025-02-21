class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        row, col = len(img), len(img[0])
        new = [[0 for _ in range(col)] for _ in range(row)]
        
        # current cell and its 8 neighbors
        directions = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1),  (0, 0),  (0, 1),
                     (1, -1),  (1, 0),  (1, 1)]
        
        for i in range(row):
            for j in range(col):
                total, count = 0, 0
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < row and 0 <= y < col:  # Check if (x, y) is inbound
                        total += img[x][y]
                        count += 1
                new[i][j] = total // count 
        
        return new
        