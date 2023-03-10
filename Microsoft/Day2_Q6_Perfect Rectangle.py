# #ReviseWithArsh #6Companies30Days Challenge 2023

#Microsoft 

# 6) Perfect Rectangle.

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        xs = []
        ys = []

        for sx, sy, ex, ey, in rectangles:
            xs.append(sx)
            xs.append(ex)

            ys.append(sy)
            ys.append(ey)

        xlookup = {x: i for i, x in enumerate(sorted(set(xs)))}
        ylookup = {y: i for i, y in enumerate(sorted(set(ys)))}  

        N = len(xlookup) - 1
        M = len(ylookup) - 1

        grid = [[0] * M for _ in range(N)]

        for sx, sy, ex, ey in rectangles:
            for cx in range(xlookup[sx], xlookup[ex]):
                for cy in range(ylookup[sy], ylookup[ey]):
                    grid[cx][cy] += 1

        for row in grid:
            for cell in row:
                if cell != 1:
                    return False
        return True       