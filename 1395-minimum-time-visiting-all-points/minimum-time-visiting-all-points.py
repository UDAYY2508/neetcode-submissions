class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        res=0
        for i in range(len(points)-1):
            x1 = points[i][0]
            x2 = points[i][1]
            y1 = points[i+1][0]
            y2 = points[i+1][1]

            dis = max(abs(x1-y1),abs(x2-y2))

            res+=dis
        return res
               