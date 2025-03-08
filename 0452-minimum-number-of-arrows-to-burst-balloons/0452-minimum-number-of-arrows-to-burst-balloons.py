class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])  
        arrows = 0  
        i = 0  

        while i < len(points):
            arrow_pos = points[i][1]  
            while i < len(points) and points[i][0] <= arrow_pos:
                i += 1  
            arrows += 1  

        return arrows  
