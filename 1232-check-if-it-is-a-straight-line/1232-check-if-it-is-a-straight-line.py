class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        i = 2
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if (x1 == x2):
            for x, y in coordinates[1:]:
                if x != x1:
                    return False
        else:
            m = (y2-y1)/(x2-x1)
            for x, y in coordinates[1:]:
                if x == x1 or (y - y1) / (x - x1) != m:
                    return False
        return True